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
        for i in range(7):
            graph.add_node(i)

        graph.add_edge(0, 1, 2.3)
        graph.add_edge(0, 3, 3.1)
        graph.add_edge(1, 2, 1.9)
        graph.add_edge(2, 3, 5.2)
        graph.add_edge(2, 6, 8.4)
        graph.add_edge(3, 0, 2.0)
        graph.add_edge(3, 6, 5.4)
        graph.add_edge(4, 3, 2.7)
        graph.add_edge(4, 5, 3.6)
        graph.add_edge(5, 4, 4.8)
        graph_algo = GraphAlgo(graph)
        self.assertEqual(graph, graph_algo.get_graph())

    def test_load_from_json(self):
        self.graph = DiGraph()
        for i in range(4):
            self.graph.add_node(i)
        self.graph.add_edge(0, 1, 3.9)
        self.graph.add_edge(1, 0, 1.8)
        self.graph.add_edge(1, 2, 2.1)
        self.graph.add_edge(1, 3, 5.6)
        self.graph.add_edge(2, 3, 4.5)
        graph_algo = GraphAlgo()
        self.assertTrue(graph_algo.load_from_json('../data/T0.json'))
        self.assertEqual(self.graph, graph_algo.get_graph())
        self.assertFalse(graph_algo.load_from_json('../data/sdasdas.json'))

    def test_shortest_path(self):
        graph = graph_creator()
        algo = GraphAlgo(graph)
        self.assertEqual((8.5, [0, 3, 6]), algo.shortest_path(0, 6))
        self.assertEqual((11.9, [7, 6, 3, 0, 1, 2]), algo.shortest_path(7, 2))
        self.assertEqual((13.700000000000001, [5, 4, 3, 0, 1, 2]), algo.shortest_path(5, 2))
        self.assertEqual(11.9, algo.shortest_path(7, 2)[0])
        self.assertEqual(7.7,  algo.shortest_path(7, 0)[0])
        self.assertEqual(0, algo.shortest_path(0, 0)[0], " path between the same node -> 0")
        self.assertEqual(float('inf'), algo.shortest_path(0, 9)[0], " 9 node that not exist ")
        self.assertEqual(float('inf'), algo.shortest_path(10, 20)[0], "2 nodes that not exist in the graph")

        # remove the edge that connects the 4 node to the other
        graph.remove_edge(5, 4)
        self.assertEqual((float('inf'), []), algo.shortest_path(6, 4), "there is not path between them ")
        self.assertEqual(7.7, algo.shortest_path(7, 0)[0])
        # remove node 3 -
        graph.remove_node(3)
        self.assertEqual((float('inf'), []), algo.shortest_path(7, 0), " there is not path between them ")
        graph.add_edge(8, 9, 5.2)
        self.assertEqual((float('inf'), []), algo.shortest_path(8, 9), "this nodes that noe exist in the graph")

    def test_connected_component(self):
        self.graph = DiGraph()
        for i in range(8):
            self.graph.add_node(i)
        #     0-1-2
        self.graph.add_edge(0, 1, 5)
        self.graph.add_edge(1, 2, 2.3)
        self.graph.add_edge(2, 0, 1.9)
        #  3
        self.graph.add_edge(2, 3, 1.3)
        # 4-5-6-7
        self.graph.add_edge(4, 5, 5.5)
        self.graph.add_edge(5, 6, 3.2)
        self.graph.add_edge(6, 7, 4.5)
        self.graph.add_edge(7, 4, 1.8)
        algo = GraphAlgo(self.graph)
        # check the connected component 0->1->2
        count_scc: list = algo.connected_component(0)
        self.assertEqual([0, 1, 2], count_scc)
        count_scc: list = algo.connected_component(1)
        self.assertEqual([1, 2, 0], count_scc)
        # 3
        count_scc: list = algo.connected_component(3)
        self.assertEqual([3], count_scc)
        # check the connected component 4->5->6->7
        count_scc: list = algo.connected_component(4)
        self.assertEqual([4, 5, 6, 7], count_scc)
        count_scc: list = algo.connected_component(6)
        self.assertEqual([6, 7, 4, 5], count_scc)
        # remove node 6 = [4], [5], [7]
        self.graph.remove_node(6)
        # there is no component
        count_scc: list = algo.connected_component(6)
        self.assertEqual([], count_scc)
        count_scc: list = algo.connected_component(4)
        self.assertEqual([4], count_scc)

    def test_connected_components(self):
        self.graph = DiGraph()
        for i in range(8):
            self.graph.add_node(i)
        #     0-1-2
        self.graph.add_edge(0, 1, 5)
        self.graph.add_edge(1, 2, 2.3)
        self.graph.add_edge(2, 0, 1.9)
        #  3
        self.graph.add_edge(2, 3, 1.3)
        # 4->5->6->7
        self.graph.add_edge(4, 5, 5.5)
        self.graph.add_edge(5, 6, 3.2)
        self.graph.add_edge(6, 7, 4.5)
        self.graph.add_edge(7, 4, 1.8)
        algo = GraphAlgo(self.graph)
        list_temp = algo.connected_components()
        list_actual = [[4, 5, 6, 7], [0, 1, 2], [3]]
        self.assertEqual(list_temp, list_actual)
        count_scc: list_temp = algo.connected_components()
        self.assertTrue(count_scc.__contains__([0, 1, 2]))
        self.assertTrue(count_scc.__contains__([3]))
        self.assertTrue(count_scc.__contains__([4, 5, 6, 7]))

    def test_plot_graph(self):

        algo = GraphAlgo(graph_creator())
        algo.plot_graph()


if __name__ == '__main__':
    unittest.main()
