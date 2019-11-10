import KBEngine
from interfaces.GameObject import GameObject


class Avatar(KBEngine.Proxy, GameObject):
    """
    角色实体
    """

    def __init__(self):
        KBEngine.Proxy.__init__(self)
        GameObject.__init__(self)

        self.accountEntity = None
        self.cellData["dbid"] = self.databaseID
        self.name = self.cellDatap["name"]
