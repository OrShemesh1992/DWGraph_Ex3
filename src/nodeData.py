class nodeData:
    # In this class we have implemented operations at a node (vertex) in a weighted graph (directional).
    # id, location, weight, tag of each vertex.
    def __init__(self, key: int, pos: tuple =None):
        self.__id = key
        self.weight = 0
        self.__pos = pos
        self.tag = 0
        self.info = ""
        self.in_edges = 0
        self.out_edges = 0

    def __eq__(self, object: object) -> bool:
        if object == None:
            return False

        if self.in_edges != object.in_edges:
            return False

        if self.out_edges != object.out_edges:
            return False

        if self.__id != object.getId():
            return False

        if self.__pos != object.getPos():
            return False

        return True

    def getId(self) -> int:
        return self.__id

    def getPos(self) -> tuple:
        return self.__pos

    def setPos(self, pos: tuple):
        self.__pos=pos

    def __repr__(self):
        return str(self.__id) + ": |edges out| " + str(self.out_edges) + " |edges in| " + str(self.in_edges)