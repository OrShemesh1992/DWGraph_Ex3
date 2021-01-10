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
    graph.add_node(4)
    graph.add_edge(0, 1, 5)
    graph.add_edge(1, 2, 1)
    graph.add_edge(2, 0, 2)
    graph.add_edge(0, 4, 2)
    graph.add_edge(4, 3, 2)
    graph.add_edge(3, 4, 2)
    algo = GraphAlgo(graph)
    print(algo.get_graph())
    print(algo.connected_components())
    print(algo.connected_component(4))
