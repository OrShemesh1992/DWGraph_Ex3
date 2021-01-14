from edgeData import edgeData
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
from nodeData import nodeData

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

    # creat a new graph
    graph1 = DiGraph()
    graph1.add_node(0)
    graph1.add_node(1)
    graph1.add_node(2)
    graph1.add_node(3)
    graph1.add_node(4)
    graph1.add_edge(0, 1, 5)
    graph1.add_edge(1, 2, 1)
    graph1.add_edge(2, 0, 2)
    graph1.add_edge(0, 4, 2)
    graph1.add_edge(4, 3, 2)
    graph1.add_edge(3, 2, 2)


    node = nodeData(1,(20,5,4))

    node1 = nodeData(1)


    print(graph1 == graph)

    print(node==node1)