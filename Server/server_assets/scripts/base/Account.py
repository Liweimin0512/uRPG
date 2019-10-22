# -*- coding: utf-8 -*-
import time

import KBEngine
from AVATAR_INFO import TAvatarInfo
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
		DEBUG_MSG("Account[%i].reqAvatarList: size=%i."%(self.id, len(self.characters)))
		self.client.onReqAvatarList(self.characters)

	def reqCreateAvatar(self, name, roleType):
		if len(self.characters) >= 3:
			# 角色超上限
			DEBUG_MSG("Account[%i].reqCreateAvatar:%s. character=%s.\n" % (self.id, name, self.characters))

			avatarinfo = TAvatarInfo()
			avatarinfo.extend([0 , "", 0, 0])
			self.client.onCreateAvatarResult(3, avatarinfo)
			return

	def reqRemoveAvatar(self, name):
		"""
		请求删除一个角色
		:param name:
		:return:
		"""
		DEBUG_MSG("Account[%i].reqRemoveAvatar: %s" % (self.id, name))
		found = 0
		for key, info in self.characters.items():
			if info[1] == name:
				del self.characters[key]
				found = key
				break

		self.client.onRemoveAvatar(found)

	def reqSelectAvatar(self, dbid):
		"""
		选择某个角色时候，获取详细信息。并设为选中角色
		:param dbid:
		:return:
		"""
		pass

	def reqEnterGame(self, dbid):
		"""
		选择摸个角色，请求进入游戏
		:param dbid:角色DBid
		"""
		DEBUG_MSG("Account[%i].selectAvatarGame:%i. self.activeAvatar=%s" % (self.id, dbid, self.activeAvatar))
		# 注意:使用giveClientTo的entity必须是当前baseapp上的entity
		if self.activeAvatar is None:
			if dbid in self.characters:
				#self.lastSelCharacter = dbid
				# 由于需要从数据库加载角色，因此是一个异步过程，加载成功或者失败会调用__onAvatarCreated接口
				# 当角色创建好之后，account会调用giveClientTo将客户端控制权（可理解为网络连接与某个实体的绑定）切换到Avatar身上，
				# 之后客户端各种输入输出都通过服务器上这个Avatar来代理，任何proxy实体获得控制权都会调用onEntitiesEnabled
				# Avatar继承了Teleport，Teleport.onEntitiesEnabled会将玩家创建在具体的场景中
				KBEngine.createEntityFromDBID("Avatar", dbid, self.__onAvatarCreated)
			else:
				ERROR_MSG("Account[%i]::selectAvatarGame: not found dbid(%i)" % (self.id, dbid))
		else:
			self.giveClientTo(self.activeAvatar)

	#------------------------------
	#         Callbacks
	#------------------------------

	def onTimer(self, id, userArg):
		"""
		KBEngine method.
		使用addTimer后， 当时间到达则该接口被调用
		@param id		: addTimer 的返回值ID
		@param userArg	: addTimer 最后一个参数所给入的数据
		"""
		DEBUG_MSG(id, userArg)
		
	def onClientEnabled(self):
		"""
		KBEngine method.
		该entity被正式激活为可使用， 此时entity已经建立了client对应实体， 可以在此创建它的
		cell部分。
		"""
		INFO_MSG("account[%i] entities enable. entityCall:%s" % (self.id, self.client))

	def onLogOnAttempt(self, ip, port, password):
		"""
		KBEngine method.
		客户端登陆失败时会回调到这里
		"""
		INFO_MSG(ip, port, password)
		return KBEngine.LOG_ON_ACCEPT
		
	def onClientDeath(self):
		"""
		KBEngine method.
		客户端对应实体已经销毁
		"""
		DEBUG_MSG("Account[%i].onClientDeath:" % self.id)
		self.destroy()

	def onDestroy(self):
		"""
		entity销毁时回调
		"""
		pass

	def _onAvatarCreated(self, baseRef, dbid, wasActive):
		"""
		选择角色进入游戏时被回调
		:param baseRef:
		:param dbid:
		:param wasActive:
		:return:
		"""
		pass

	def _onAvatarSaved(self, success, avatar):
		"""
		新建角色写入服务器回调
		:param success:
		:param avatar:
		"""
		INFO_MSG('Account::_onAvatarSaved:(%i) create avatar state: %i, %s, %i' % (
			self.id, success, avatar.cellData["name"], avatar.databaseID))

		# 如果此时账号已经销毁， 角色已经无法被记录则我们清除这个角色
		if self.isDestroyed:
			if avatar:
				avatar.destroy(True)

			return

		avatarinfo = TAvatarInfo()
		avatarinfo.extend([0, "", 0, 0])

		errorcode = 0
		if success:
			avatarinfo[0] = avatar.databaseID
			avatarinfo[1] = avatar.cellData["name"]
			avatarinfo[2] = avatar.roleType
			avatarinfo[3] = 1
			self.characters[avatar.databaseID] = avatarinfo
			self.writeToDB()
		else:
			avatarinfo[1] = "创建失败了"
			errorcode = 4

		avatar.destroy()

		if self.client:
			self.client.onCreateAvatarResult(errorcode, avatarinfo)
