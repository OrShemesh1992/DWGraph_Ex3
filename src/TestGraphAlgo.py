import unittest
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from src.nodeData import nodeData


def graph_creator() -> DiGraph:
    graph = DiGraph()
    for x in range(8):
        graph.add_node(x)

    graph.add_edge(0, 1, 2.3)
    graph.add_edge(0, 3, 3.1)
    graph.add_edge(1, 2, 1.9)
    graph.add_edge(2, 3, 5.2)
    graph.add_edge(2, 7, 8.4)
    graph.add_edge(3, 0, 2.0)
    graph.add_edge(3, 6, 5.4)
    graph.add_edge(4, 3, 2.7)
    graph.add_edge(4, 5, 3.6)
    graph.add_edge(5, 4, 4.8)
    graph.add_edge(6, 3, 4.7)
    graph.add_edge(6, 5, 2.5)
    graph.add_edge(6, 7, 1.2)
    graph.add_edge(7, 6, 1.0)
    graph.add_edge(7, 2, 12.0)

    return graph


class MyTestCase(unittest.TestCase):
    graph = DiGraph()

    def test_get_graph(self):
        graph = DiGraph()
        self.assertEqual(True, False)

    def test_load_from_json(self):
        graph = DiGraph()
        self.assertEqual(True, False)

    def test_save_to_json(self):
        graph = DiGraph()
        self.assertEqual(True, False)

    def test_shortest_path(self):
        graph = graph_creator()
        algo = GraphAlgo(graph)
        self.assertEqual((8.5, [0, 3, 6]), algo.shortest_path(0, 6))
        self.assertEqual((11.9, [7, 6, 3, 0, 1, 2]), algo.shortest_path(7, 2))
        self.assertEqual((13.700000000000001, [5, 4, 3, 0, 1, 2]), algo.shortest_path(5, 2))
        self.assertEqual(11.9, algo.shortest_path(7, 2)[0])
        self.assertEqual(7.7,  algo.shortest_path(7, 0)[0])
        self.assertEqual(0, algo.shortest_path(0, 0)[0], " path between the same node -> 0")
        self.assertEqual(-1, algo.shortest_path(0, 9)[0], " 9 node that not exist -> -1")
        self.assertEqual(-1, algo.shortest_path(10, 20)[0], "2 nodes that not exist in the graph")

        # remove the edge that connects the 4 node to the other
        graph.remove_edge(5, 4)
        self.assertEqual(-1, algo.shortest_path(6, 4)[0], "there is not path between them -> -1")
        self.assertEqual(7.7, algo.shortest_path(7, 0)[0])
        # remove node 3 -
        graph.remove_node(3)
        self.assertEqual(-1, algo.shortest_path(7, 0)[0], " there is not path between them  -> -1")
        graph.add_edge(8, 9, 5.2)
        self.assertEqual(-1, algo.shortest_path(8, 9)[0], "this nodes that noe exist in the graph")

    def test_connected_component(self):
        graph = DiGraph()
        self.assertEqual(True, False)

    def test_connected_components(self):
            graph = DiGraph()
            self.assertEqual(True, False)

    def test_plot_graph(self):
            graph = DiGraph()
            self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
