# -*- coding: utf-8 -*-
import KBEngine
import time
from KBEDebug import *

class CombatComponent(KBEngine.EntityComponent):
	'''
	战斗相关组件
	只有拥有此组件的实体才参与战斗
	'''
	def __init__(self):
		KBEngine.EntityComponent.__init__(self)

	def onAttached(self, owner):
		"""
		挂载组件时候调用的方法
		"""
		self._owner = owner
		INFO_MSG("Test::onAttached(): owner=%i" % (owner.id))
		self.owner.client.component1.helloCB(111)

	def onDetached(self, owner):
		"""
		"""
		INFO_MSG("Test::onDetached(): owner=%i" % (owner.id))

	def recvDamge(self,attackerId,skillId,damageType,damage):
		pass

