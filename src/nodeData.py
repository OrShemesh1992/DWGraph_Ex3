
class nodeData:
    def __init__(self, key: int , pos: tuple):
        self.__id = key
        self.weight = 0
        self.__pos = pos
        self.tag = 0

    def getId(self) -> int:
        return self.__id

    def getPos(self) -> tuple:
        return self.__pos

    def __str__(self):
        return "nodeData(id: %s , weight: %s , pos: %s  )" % (
            self.__id, self.weight, self.__pos)