# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
# import d_spaces_person

class SpaceManager(KBEngine.Entity):
	def __init__(self):
		KBEngine.Proxy.__init__(self)

		# 初始化空间分配器
		self.initAlloc()

		KBEngine.globalData["SpaceManager"] = self

	def initAlloc(self):

		self._spaceAllocs = {}

		self._spacePerson = {}
		# self._tmpDatasperson = list(d_spaces_person.datas.keys())

	def getSpaceAllocs(self):
		return self._spaceAllocs


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
