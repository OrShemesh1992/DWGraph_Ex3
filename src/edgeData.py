class edgeData:
    def __init__(self, src: int, dest: int, w: float):
        self.__src = src
        self.__dest = dest
        self.__w = w
        self.info = ""
        self.tag = 0

    def getSrc(self) -> int :
        return self.__src
    def getDest(self) -> int:
        return self.__dest
    def getW(self) -> float:
        return self.__w

    def __repr__(self):
        return "%s" % (
             self.__w)

