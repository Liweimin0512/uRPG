import KBEngine


class Avatar(KBEngine.Proxy):
    """
    角色实体
    """

    def __init__(self):
        KBEngine.Proxy.__init__(self)

        self.accountEntity = None
        # self.cellData["dbid"] = self.databaseID
        # self.name = self.cellDatap["name"]
