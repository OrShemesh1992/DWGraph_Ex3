from GraphInterface import GraphInterface
from edgeData import edgeData
from nodeData import nodeData
from typing import Dict


class DiGraph(GraphInterface):
    def __init__(self):
        super()
        self.__nodes_graph: Dict[int, nodeData] = dict()
        self.__edges_graph: Dict[int, Dict[int, edgeData]] = dict()
        self.__mc = 0
        self.__edgeSize = 0

    def v_size(self) -> int:
        return len(self.__nodes_graph)

    def e_size(self) -> int:
        return self.__edgeSize

    def get_all_v(self) -> dict:
        return self.__nodes_graph

    def all_in_edges_of_node(self, id1: int) -> dict:
        edges_graph: Dict[int, edgeData] = dict()
        for i in self.__nodes_graph:
            if id1 in self.__edges_graph.get(i):
                edges_graph.__setitem__(i, self.__edges_graph.get(i)[id1])
        return edges_graph

    def all_out_edges_of_node(self, id1: int) -> dict:
        edges_graph: Dict[int, edgeData] = dict()
        if id1 in self.__nodes_graph:
            for temp in self.__edges_graph.get(id1):
                # print("key:",temp,"value: " ,self.edges_graph.get(id1)[temp])
                edges_graph.__setitem__(temp,self.__edges_graph.get(id1)[temp])
        return edges_graph

    def get_mc(self) -> int:
        return self.__mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:

        if id1 not in self.__nodes_graph or id2 not in self.__nodes_graph:
            return False
        if id1 == id2:
            return False
        if weight < 0:
            return False
        if id2 in self.__edges_graph.get(id1):
            return False
        else:
                edge = edgeData(id1, id2, weight)
                self.__edges_graph.get(id1).__setitem__(id2, edge)
                self.__mc += 1
                self.__edgeSize += 1
                return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:

        if node_id in self.__nodes_graph:
            return False
        else:
            self.__nodes_graph.__setitem__(node_id, nodeData(node_id, pos))
            self.__edges_graph.__setitem__(node_id, dict())
            self.__mc += 1
            return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.__nodes_graph:
            return False
        else:
            edges_in = self.all_in_edges_of_node(node_id)
            edges_out = self.all_out_edges_of_node(node_id)
            self.__mc += len(edges_in)
            self.__mc += len(edges_out)
            self.__edgeSize -= len(edges_in)
            self.__edgeSize -= len(edges_out)
            for x in edges_in:
                self.__edges_graph.get(x).pop(node_id)
            self.__edges_graph.pop(node_id)
            self.__mc += 1
            self.__nodes_graph.pop(node_id)
            return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 not in self.__nodes_graph or node_id2 not in self.__nodes_graph:
            return False
        if node_id1 == node_id2:
            return False

        if node_id2 not in self.__edges_graph.get(node_id1):
            return False
        else:
            self.__edges_graph.get(node_id1).pop(node_id2)
            self.__mc += 1
            self.__edgeSize -= 1
            return True

    def __repr__(self):
        return "Graph(Vetexs: %s , Edges: %s )" % (
            self.__nodes_graph, self.__edges_graph)
