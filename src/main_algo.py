from edgeData import edgeData
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
if __name__ == '__main__':
    algo=GraphAlgo()
    algo.load_from_json("test.json")
    graph = algo.get_graph()

    print(graph.e_size())
    print(graph.v_size())

    print(algo.save_to_json("test2.json"))