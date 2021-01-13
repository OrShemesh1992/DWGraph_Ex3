# In this class we performed operations on the edges of the graph.
# Each edge consists of 2 nodes - src and dest and each edgee has a weight.

class edgeData:
    def __init__(self, src: int, dest: int, w: float):
        self.__src = src
        self.__dest = dest
        self.__w = w
        self.info = ""
        self.tag = 0

    # return the src
    def get_src(self) -> int:
        return self.__src

    # return the dest
    def get_dest(self) -> int:
        return self.__dest

    # return the weight of the edge
    def get_w(self) -> float:
        return self.__w

    def __repr__(self):
        return "%s" % (
            self.__w)
