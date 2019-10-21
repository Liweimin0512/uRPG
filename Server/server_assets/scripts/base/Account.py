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
