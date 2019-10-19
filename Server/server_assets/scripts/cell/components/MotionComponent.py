# -*- coding: utf-8 -*-
import KBEngine
import time
from KBEDebug import *

class Test(KBEngine.EntityComponent):
	'''
	移动相关组件
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

	def stopMotion(self):
		'''
		停止移动
		'''
		if self.isMoving:
			INFO_MSG("%i stop motion" % (self._owner.id))
			self._owner.cancelController("Movement")
			self.isMoving = False

	def randomWalk(self,basePos):
		'''
		随机移动
		:param basePos:移动原点
		:return:是否能够移动
		'''
		if self.isMoving:
			return False
		if time.time() < self.nextMoveTime:
			return False

