import json
import unittest
from datetime import datetime
import networkx as nx
import sys
sys.setrecursionlimit(10000)
from src.GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):

    def test_time(self):
        p = "../data/G_10000_80000_0.json"
        with open(p, 'r') as file:
            s = json.load(file)
        g = nx.DiGraph()
        for node in s["Nodes"]:
                g.add_node(node['id'])
        for edge in s["Edges"]:
            g.add_edge(edge["src"], edge["dest"],  w=edge["w"])

        start = datetime.now()
        nx.shortest_path(g, 1, 5)
        stop = datetime.now()
        result = stop - start
        print(" run time for shortest_path:", result)

        start = datetime.now()
        nx.strongly_connected_components(g)
        stop = datetime.now()
        result = stop - start
        print("run time for connected_components", result)

        a = GraphAlgo()
        self.assertTrue(a.load_from_json(p))

        start = datetime.now()
        a.shortest_path(1, 5)
        stop = datetime.now()
        result = stop - start
        print(" run time for shortest_path:", result)

        start = datetime.now()
        a.connected_components()
        stop = datetime.now()
        result = stop - start
        print("run time for connected_components:", result)

        start = datetime.now()
        a.connected_component(9)
        stop = datetime.now()
        result = stop - start
        print("run time for connected_component:", result)


if __name__ == '__main__':
    unittest.main()
