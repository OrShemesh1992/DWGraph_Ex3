import timeit
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
import sys
sys.setrecursionlimit(10000)


class compare:

    def __init__(self):
        self.g = DiGraph()
        self.graph = GraphAlgo(self.g)

    def getGraph(self):
        return self.graph.graph

    def json_runtime(self, str = None):
        self.graph.load_from_json(str)
        start = timeit.default_timer()
        stop = timeit.default_timer()
        print("run time from jsom file", stop - start)

    def shortest_path(self, str = None):
        self.graph.load_from_json(str)
        start = timeit.default_timer()
        f = self.graph.shortest_path(1, 5)
        stop = timeit.default_timer()
        weight = f[0]
        path = f[1]
        print("shortest path :\n")
        print(f"The shortest path between {1} and {5} is : {weight} \n"
        f"And the path is : {path} ")
        print(" run time for shortest_path:", stop - start)

    def connected(self, str=None):
        start = timeit.default_timer()
        self.graph.load_from_json(str)
        print("connected component :\n")
        component = self.graph.connected_component(1)
        stop = timeit.default_timer()

        print(f"The strongly component of node : {1} is : \n"
        f"{component}\n")
        print(" run time for connected component :", stop - start)
        print("connected components :\n")
        start = timeit.default_timer()

        components = self.graph.connected_components()
        print(f"The strongly components of graph is : \n"
        f"{components}\n")
        stop = timeit.default_timer()
        print(" run time for connected_components:", stop - start)


if __name__ == '__main__':
    G = compare()

    print("6")
    G.shortest_path('../data/G_30000_240000_0.json')
    G.connected('../data/G_30000_240000_0.json')
    G.json_runtime('../data/G_30000_240000_0.json')

    ("5")
    G.shortest_path('../data/G_20000_160000_0.json')
    G.connected('../data/G_20000_160000_0.json')
    G.json_runtime('../data/G_20000_160000_0.json')

    print("4")
    G.shortest_path('../data/G_10000_80000_0.json')
    G.connected('../data/G_10000_80000_0.json')
    G.json_runtime('../data/G_10000_80000_0.json')

    print("3")
    G.shortest_path('../data/G_1000_8000_0.json')
    G.connected('../data/G_1000_8000_0.json')
    G.json_runtime('../data/G_1000_8000_0.json')
    print("2")

    G.shortest_path('../data/G_100_800_0.json')
    G.connected('../data/G_100_800_0.json')
    G.json_runtime('../data/G_100_800_0.json')

    print("1")

    G.shortest_path('../data/G_10_80_0.json')
    G.connected('../data/G_10_80_0.json')
    G.json_runtime('../data/G_10_80_0.json')