# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class InventoryComponent(KBEngine.EntityComponent):
    def __init__(self,entity):
        self._entity = entity
        self.invIndex2Uids = [0]*12

    def addItem(self,itemId,ItemCount = 1):
        pass

    def removeItem(self,itemUUID,ItemCount):
        pass


    def UseItemFromInvTile(self,item):
        if self.GetActiveItem() :
            return

        if item and self._entity.components.playeractionpicker:
            if self.GetActiveItem():
                actions = self._entity.components.playeractionpicker.GetUseItemActions(item,self.GetActiveItem(),True)
                if actions :
                    self._entity.components.locomotor.PushAction(actions[1],True)

    def EquipHasTag(self,tag):
        for k, v in self.equipslots.items():
            if v.HasTag(tag):
                return True