# -*- coding:utf-8 -*-
import KBEngine
import GlobalConst
from KBEDebug import *


class TAvatarInfo(list):
    """
    """
    def __init__(self):
        """
        """
        list.__init__(self)

    def asDict(self):
        data = {
            "dbid"      :self[0],
            "name"      :self[1],
            "raceType"  :self[2],
            "level"     :self[3],
        }
        return data

    def CreateFromDict(self,dictData):
        self.extend([dictData["dbid"], dictData["name"], dictData["raceType"], dictData["level"]])
        return self


class AVATAR_INFO_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self,dct):
        return TAvatarInfo().CreateFromDict(dct)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, TAvatarInfo)


avatar_info_inst = AVATAR_INFO_PICKLER()


class TAvatarInfoList(dict):
    """
    """

    def __init__(self):
        """
        """
        dict.__init__(self)

    def asDict(self):
        datas = []
        dct = {"values": datas}

        for key, val in self.items():
            datas.append(val)

        return dct

    def createFromDict(self, dictData):
        for data in dictData["values"]:
            self[data[0]] = data
        return self


class AVATAR_INFO_LIST_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dct):
        return TAvatarInfoList().createFromDict(dct)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, TAvatarInfoList)


avatar_info_list_inst = AVATAR_INFO_LIST_PICKLER()