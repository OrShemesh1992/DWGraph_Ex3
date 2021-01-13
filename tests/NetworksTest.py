import json
import unittest
import networkx as nx
import sys
import timeit


class MyTestCase(unittest.TestCase):

    def test_time(self):
        p = "../data/G_10_80_0.json"
        with open(p, 'r') as file:
            s = json.load(file)
        g = nx.DiGraph()
        for node in s["Nodes"]:
                g.add_node(int(node['id']))
        for edge in s["Edges"]:
            g.add_edge(int(edge["src"]), int(edge["dest"]),  weight=float(edge["w"]))

        # print(g.number_of_nodes())
        # print(len(g.edges))
        print(nx.shortest_path(g,source=1,target=5,method="dijkstra",weight="weight"))
        # self.assertTrue(a.load_from_json(p))
        #
        start = timeit.default_timer()
        # a.shortest_path(1, 5)
        stop = timeit.default_timer()

        print(" run time for shortest_path:", stop - start)

        start = timeit.default_timer()
        com=list(nx.strongly_connected_components(g))
        print(com)
        stop = timeit.default_timer()
        print("run time for connected_components:", stop - start)

        # start = timeit.default_timer()
        # nx.connected_component(9)
        # stop = timeit.default_timer()
        # print("run time for connected_component:", stop - start)


if __name__ == '__main__':
    unittest.main()
