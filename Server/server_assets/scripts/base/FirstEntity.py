# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class FirstEntity(KBEngine.Proxy):
    """
    第一个实体的base部分的实现
    """

    def __init__(self):
        KBEngine.Entity.__init__(self)

    def onClientEnabled(self):
        '''
        该Entity被正式激活为可使用，此时entity已经建立了client对应实体
        :return:
        '''
        # 客户端一旦连接，就将其放入FirstSpace空间
        first_space = KBEngine.globalData["FirstSpace"]
        self.createCellEntity(first_space.cell)