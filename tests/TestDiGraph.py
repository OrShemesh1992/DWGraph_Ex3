import unittest

from src.DiGraph import DiGraph


def graph_creator() -> DiGraph:
    graph = DiGraph()
    for x in range(8):
        graph.add_node(x)

    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 3, 3)
    graph.add_edge(1, 2, 1)
    graph.add_edge(2, 3, 5)
    graph.add_edge(2, 7, 8)
    graph.add_edge(3, 0, 2)
    graph.add_edge(3, 6, 5)
    graph.add_edge(4, 3, 2)
    graph.add_edge(4, 5, 3)
    graph.add_edge(5, 4, 4)
    graph.add_edge(6, 3, 4)
    graph.add_edge(6, 5, 2)
    graph.add_edge(7, 6, 1)

    return graph


class MyTestCase(unittest.TestCase):
    graph = graph_creator()

    def test_v_size(self):
        graph = graph_creator()
        self.assertEqual(8, self.graph.v_size(), "the number of the nodes in the graph")
        graph.remove_edge(3, 6)
        self.assertEqual(8, graph.v_size(), "remove edge the num of nodes not change")
        graph.remove_node(2)
        self.assertEqual(7, graph.v_size(), "remove node from the graph")
        graph.remove_node(2)
        self.assertEqual(7, graph.v_size(), "remove node that not exist")


    def test_e_size(self):
        graph = graph_creator()
        self.assertEqual(13, self.graph.e_size(), "number of the edge in the graph")
        graph.remove_edge(0, 1)
        graph.remove_edge(0, 3)
        self.assertEqual(11, graph.e_size())
        graph.add_edge(10, 10, 2)
        graph.add_edge(0, 0, 2)
        self.assertEqual(11, graph.e_size(), "add edges with the same nodes and the nods not exist")

    def test_get_all_v(self):
        graph = DiGraph()
        graph.add_node(0)
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        nodes = graph.get_all_v()
        self.assertEqual(len(nodes.values()), 4)
        graph.add_node(3)
        self.assertEqual(len(nodes.values()), 4, "add node that exist")

    def test_all_in_edges_of_node(self):
        graph = DiGraph()
        graph.add_node(0)
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_edge(0, 1, 5)
        graph.add_edge(1, 2, 3)
        graph.add_edge(2, 0, 1)
        graph.add_edge(2, 1, 4)
        graph.add_edge(2, 3, 3)
        graph.add_edge(3, 2, 2)
        edges_in = graph.all_in_edges_of_node(1)
        self.assertEqual(len(edges_in.values()), 2, "the number of the edges that in to the node 1")
        graph.remove_node(2)
        edges_in = graph.all_in_edges_of_node(1)
        self.assertEqual(len(edges_in.values()), 1, "the new number of the edges that in to the node 1")

    def test_all_out_edges_of_node(self):
        graph = DiGraph()
        graph.add_node(0)
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_edge(0, 1, 5)
        graph.add_edge(1, 2, 3)
        graph.add_edge(2, 0, 1)
        graph.add_edge(2, 1, 4)
        graph.add_edge(2, 3, 3)
        graph.add_edge(3, 2, 2)
        edges_out = graph.all_out_edges_of_node(0)
        self.assertEqual(len(edges_out.values()), 1, "the number of the edges that in to the node 1")
        graph.remove_node(1)
        edges_out = graph.all_out_edges_of_node(0)
        self.assertEqual(len(edges_out.values()), 0, "the new number of the edges that in to the node 1")

    def test_get_mc(self):
        graph = graph_creator()
        self.assertEqual(21, graph.get_mc())
        graph.remove_edge(3, 6)
        self.assertEqual(22, graph.get_mc())
        graph.remove_edge(3, 6)
        self.assertEqual(22, graph.get_mc(), "remove edge that not exist -do nothing")
        graph.remove_node(1)
        graph.remove_node(4)
        self.assertEqual(29, graph.get_mc(), "remove 2 nodes that exist in the graph")
        graph.remove_node(1)
        self.assertEqual(29, graph.get_mc(), "remove node that not exist -do nothing")

    def test_add_edge(self):
        graph = graph_creator()
        self.assertEqual(False, graph.add_edge(0, 1, 2), "add edge that already exist")
        self.assertEqual(True, graph.add_edge(0, 4, 2)), "add edge that not exist"
        self.assertEqual(False, graph.add_edge(5, 4, 7), "change the weight to edge that exist-false")
        self.assertEqual(False, graph.add_edge(10, 1, 2), "add edge with node that not exist")
        graph.remove_node(5)
        graph.remove_node(6)
        self.assertEqual(False, graph.add_edge(5, 6, 2), "add edge with nodes that not exist")
        graph.add_node(5)
        graph.add_node(6)
        self.assertEqual(True, graph.add_edge(5, 6, 2), "nodes that exist")
        self.assertEqual(False, graph.add_edge(5, 6, 2), "add edge that exist with same weight")
        self.assertEqual(False, graph.add_edge(5, 5, 2), "the same edge with same weight-false")

    def test_add_node(self):
        graph = DiGraph()   # creat a new graph
        graph.add_node(0)
        graph.add_node(1)
        graph.add_node(2)
        self.assertEqual(3, graph.get_mc(), "add 3 nodes to the graph ")
        graph.add_node(2)
        self.assertEqual(3, graph.get_mc(), " add node that already exist")
        graph.remove_node(0)
        self.assertEqual(4, graph.get_mc(), "remove node that exist")
        self.assertEqual(False, graph.add_edge(0, 1, 5), " node 0 not exist")
        graph.add_node(0)
        self.assertEqual(True, graph.add_edge(0, 1, 5), " node 0 exist")
        self.assertEqual(6, graph.get_mc())

    def test_remove_node(self):
        graph = graph_creator()
        self.assertEqual(21, graph.get_mc())
        graph.remove_node(0)
        self.assertEqual(10, graph.e_size())
        self.assertEqual(7, graph.v_size())
        graph.remove_node(0)
        self.assertEqual(25, graph.get_mc(), "remove node that removed- do nothing")
        self.assertEqual(7, graph.v_size(), "remove node that removed- do nothing")
        graph.remove_node(100)
        self.assertEqual(25, graph.get_mc())

    def test_remove_edge(self):
        graph = graph_creator()
        self.assertEqual(21, graph.get_mc())
        graph.remove_edge(0, 3)
        graph.remove_edge(0, 1)
        self.assertEqual(11, graph.e_size(), "remove edges that exist in the graph")
        self.assertEqual(23, graph.get_mc())
        graph.remove_edge(0, 3)  # remove edge that not exist
        graph.remove_edge(10, 13)  # remove edge that not exist with nodes that not exist
        self.assertEqual(11, graph.e_size())
        # add edge with the same node ane remove- do nothing
        graph.add_edge(10, 10, 2)
        graph.remove_edge(10, 10)
        self.assertEqual(11, graph.e_size())






if __name__ == '__main__':
    unittest.main()