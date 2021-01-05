from edgeData import edgeData
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
if __name__ == '__main__':
    # algo=GraphAlgo()
    # algo.load_from_json("test.json")
    # graph = algo.get_graph()
    #
    # print(graph.e_size())
    # print(graph.v_size())
    #
    # print(algo.save_to_json("test2.json"))
    graph = DiGraph()  # creat a new graph
    graph.add_node(0)
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_edge(3, 1, 5)
    graph.add_edge(3, 2, 1)
    graph.add_edge(2, 1, 2)
    algo = GraphAlgo(graph)
    print(algo.shortest_path(3,1))
