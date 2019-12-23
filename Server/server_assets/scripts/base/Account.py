# -*- coding: utf-8 -*-
import time

import GlobalConst
import KBEngine
import d_race
import d_spaces
from AVATAR_DATA import TAvatarData
from AVATAR_INFOS import TAvatarInfos
from KBEDebug import *


class Account(KBEngine.Proxy):
    """
	账户实体
	客户端登录成功，服务器自动创建此实体，通过此实体与客户端交互
	"""

    def __init__(self):
        KBEngine.Proxy.__init__(self)
        self.activeAvatar = None
        self.relogin = time.time()

    def reqAvatarList(self):
        """
		客户端请求查询角色列表
		:return:角色列表
		"""
        DEBUG_MSG("Account[%i].reqAvatarList: size=%i." % (self.id, len(self.characters)))
        self.client.onReqAvatarList(self.characters)

    def reqCreateAvatar(self, name, raceType):
        """
        客户端请求创建角色
        :param name: 角色名
        :param raceType: 角色种族
        :return:角色spaceUType
        """
        avatarInfo = TAvatarInfos()
        avatarInfo.extend([0, "", 0, 0, TAvatarData().createFromDict({"param1": 0, "param2": b''})])

        # 服务器重名检测
        """
        if name in all_avatar_names:
        	retcode = 2
        	self.client.onCreateAvatarResult(retcode, avatarinfo)
        	return
        """

        if len(self.characters) >= 3:
            DEBUG_MSG("Account[%i].reqCreateAvatar:%s. character=%s.max!!!\n" % (self.id, name, self.characters))
            self.client.onCreateAvatarResult(3, avatarInfo)
            return

        spaceUType = GlobalConst.g_demoMaps.get(self.getClientDatas()[0], 1)

        # 如果是机器人登陆，随机扔进一个场景
        if self.getClientType() == 6:
            while True:
                spaceName = random.choice(list(GlobalConst.g_demoMaps.keys()))
                if len(spaceName) > 0:
                    spaceUType = GlobalConst.g_demoMaps[spaceName]
                    break

        spaceData = d_spaces.datas.get(spaceUType)

        props = {
            "name": name,
            "raceType": raceType,
            "level": 1,
            "spaceUType": spaceUType,
            "position": spaceData.get("spawnPos", (0, -5, -10)),
        }

        avatar = KBEngine.createEntityLocally("Avatar", props)
        if avatar:
            avatar.writeToDB(self.onAvatarSaved)

        DEBUG_MSG("Account[%i].reqCreateAvatar:%s. spaceUType=%i, spawnPos=%s.\n" % (
            self.id, name, avatar.cellData["spaceUType"], spaceData.get("spawnPos", (0, 0, 0))))

    def reqRemoveAvatar(self, name):
        """
        请求删除一个角色
        :param name:角色名
        :return:删除的角色dbid
        """
        DEBUG_MSG("Account[%i].reqRemoveAvatar: %s" % (self.id, name))
        found = 0
        for key, info in self.characters.items():
            if info[1] == name:
                del self.characters[key]
                found = key
                break

        self.client.onRemoveAvatar(found)

    def reqRemoveAvatarDBID(self, dbid):
        """
        exposed.
        客户端请求删除一个角色
        """
        DEBUG_MSG("Account[%i].reqRemoveAvatar: %s" % (self.id, dbid))
        found = 0

        if dbid in self.characters:
            del self.characters[dbid]
            found = dbid

        self.client.onRemoveAvatar(found)

    def reqEnterGame(self, dbid):
        """
        选择摸个角色，请求进入游戏
        :param dbid:角色DBid
        """
        DEBUG_MSG("Account[%i].reqEnterGame:%i. self.activeAvatar=%s" % (self.id, dbid, self.activeAvatar))
        # 注意:使用giveClientTo的entity必须是当前baseapp上的entity
        if self.activeAvatar is None:
            if dbid in self.characters:
                self.lastSelCharacter = dbid
                # 由于需要从数据库加载角色，因此是一个异步过程，加载成功或者失败会调用__onAvatarCreated接口
                # 当角色创建好之后，account会调用giveClientTo将客户端控制权（可理解为网络连接与某个实体的绑定）切换到Avatar身上，
                # 之后客户端各种输入输出都通过服务器上这个Avatar来代理，任何proxy实体获得控制权都会调用onEntitiesEnabled
                # Avatar继承了Teleport，Teleport.onEntitiesEnabled会将玩家创建在具体的场景中
                KBEngine.createEntityFromDBID("Avatar", dbid, self.onAvatarCreated)
            else:
                ERROR_MSG("Account[%i]::reqEnterGame : not found dbid(%i)" % (self.id, dbid))
        else:
            self.giveClientTo(self.activeAvatar)

    # --------------------------------------------------------------------------------------------
    #                              Callbacks
    # --------------------------------------------------------------------------------------------

    def onClientEnabled(self):
        """
        KBEngine method.
        该entity被正式激活为可使用， 此时entity已经建立了client对应实体， 可以在此创建它的
        cell部分。
        """
        # INFO_MSG("account[%i] entities enable. entityCall:%s"
        #          % (self.id, self.client, self.getClientType(), self.getClientDatas(), self.activeAvatar,
        #             self.__ACCOUNT_NAME__))

    def onLogOnAttempt(self, ip, port, password):
        """
        KBEngine method.
        客户端登陆失败时会回调到这里
        """
        INFO_MSG("Account[%i]::onLogOnAttempt: ip=%s, port=%i, self_client=%s" % (self.id, ip, port, self.client))
        """
        if self.activeAvatar != None:
        	return KBEngine.LOG_ON_REJECT

        if ip == self.lastClientIpAddr and password == self.password:
        	return KBEngine.LOG_ON_ACCEPT
        else:
        	return KBEngine.LOG_ON_REJECT
        """
        # 如果一个在线的账号被一个客户端登陆并且onLogOnAttempt返回允许
        # 那么会踢掉之前的客户端连接
        # 那么此时self.activeAvatar可能不为None， 常规的流程是销毁这个角色等新客户端上来重新选择角色进入
        if self.activeAvatar:
            if self.activeAvatar.client is not None:
                self.activeAvatar.giveClientTo(self)

            self.relogin = time.time()
            self.activeAvatar.destroySelf()
            self.activeAvatar = None

        return KBEngine.LOG_ON_ACCEPT

    def onClientDeath(self):
        """
        KBEngine method.
        客户端对应实体已经销毁
        """
        if self.activeAvatar:
            self.activeAvatar.accountEntity = None
            self.activeAvatar = None

        DEBUG_MSG("Account[%i].onClientDeath:" % self.id)
        self.destroy()

    def onDestroy(self):
        """
        entity销毁时回调
        """
        DEBUG_MSG("Account::onDestroy: %i." % self.id)

        if self.activeAvatar:
            self.activeAvatar.accountEntity = None

            try:
                self.activeAvatar.destroySelf()
            except:
                pass

            self.activeAvatar = None

    def onAvatarCreated(self, baseRef, dbid, wasActive):
        """
        选择角色进入游戏时被回调
        :param baseRef:
        :param dbid:
        :param wasActive:
        """
        if wasActive:
            ERROR_MSG("Account::__onAvatarCreated:(%i): this character is in world now!" % (self.id))
            return
        if baseRef is None:
            ERROR_MSG("Account::__onAvatarCreated:(%i): the character you wanted to created is not exist!" % (self.id))
            return

        avatar = KBEngine.entities.get(baseRef.id)
        if avatar is None:
            ERROR_MSG("Account::__onAvatarCreated:(%i): when character was created, it died as well!" % (self.id))
            return

        if self.isDestroyed:
            ERROR_MSG("Account::__onAvatarCreated:(%i): i dead, will the destroy of Avatar!" % (self.id))
            avatar.destroy()
            return

        info = self.characters[dbid]
        # avatar.cellData["modelID"] = d_avatar_inittab.datas[info[2]]["modelID"]
        # avatar.cellData["modelScale"] = d_avatar_inittab.datas[info[2]]["modelScale"]
        # avatar.cellData["moveSpeed"] = d_avatar_inittab.datas[info[2]]["moveSpeed"]
        avatar.accountEntity = self
        self.activeAvatar = avatar
        self.giveClientTo(avatar)

    def onAvatarSaved(self, success, avatar):
        """
        新建角色写入服务器回调
        :param success:成功
        :param avatar:角色数据
        """
        INFO_MSG('Account::onAvatarSaved:(%i) create avatar state: %i, %s, %i' % (
            self.id, success, avatar.cellData["name"], avatar.databaseID))

        # 如果此时账号已经销毁， 角色已经无法被记录则我们清除这个角色
        if self.isDestroyed:
            if avatar:
                avatar.destroy(True)
            return

        avatarinfo = TAvatarInfos()
        avatarinfo.extend([0, "", 0, 0, TAvatarData().createFromDict({"param1": 0, "param2": b''})])

        if success:
            info = TAvatarInfos()
            info.extend([avatar.databaseID, avatar.cellData["name"], avatar.raceType, 1,
                         TAvatarData().createFromDict({"param1": 1, "param2": b'1'})])
            self.characters[avatar.databaseID] = info
            avatarinfo[0] = avatar.databaseID
            avatarinfo[1] = avatar.cellData["name"]
            avatarinfo[2] = avatar.raceType
            avatarinfo[3] = 1
            self.writeToDB()
        else:
            avatarinfo[1] = "创建失败了"

        avatar.destroy()

        if self.client:
            self.client.onCreateAvatarResult(0, avatarinfo)
