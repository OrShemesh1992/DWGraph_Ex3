import timeit
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
import sys
sys.setrecursionlimit(10000)

def json_runtime():
    GraphAl = GraphAlgo()
    start = timeit.default_timer()
    GraphAl.load_from_json('../data/G_30000_240000_0.json')
    stop = timeit.default_timer()
    print("run time from jsom file", stop - start)
    print("number", len(connected_components()))

def shortest_paths():
    g = GraphAlgo()
    g.load_from_json('../data/G_30000_240000_0.json')
    print("Shortest Path ////////////////////////////////////////\n")
    dt =json_runtime()
    f = g.shortest_path(1, 5)
    print(f"my time : {dt}, path list for correct algo= {f[1]}")

def connecteds_component():
    g = GraphAlgo()
    g.load_from_json('../data/G_20000_160000_0.json')
    print("sssa")
    print("Connected Component ////////////////////////////////////////\n")
    dt = json_runtime()
    f = g.connected_component(1)
    print(f"my time : {dt}, path list for correct algo= {f[1]}")

def connected_components():
    g = GraphAlgo()
    g.load_from_json('../data/G_20000_160000_0.json')
    print("sssss")
    print("Connected Components ////////////////////////////////////////\n")
    dt = json_runtime()
    f = g.connected_component(1)
    print(f"my time : {dt}, path list for correct algo= {f[1]}")

if __name__ == '__main__':
     connected_components()

