from GraphInterface import GraphInterface

from edgeData import edgeData
from nodeData import nodeData
from typing import Dict


class DiGraph(GraphInterface):
    def __init__(self):
        super()
        self.nodes_graph: Dict[int, nodeData] = dict()
        self.edges_graph: Dict[int, Dict[int, edgeData]] = dict()
        self.mc = 0
        self.edgeSize = 0
        self.nodeSize = 0

    def v_size(self) -> int:
        return len(self.nodes_graph)

    def e_size(self) -> int:
        return self.edgeSize

    def get_all_v(self) -> dict:
        return self.nodes_graph

    def all_in_edges_of_node(self, id1: int) -> dict:
        temp: Dict[int, Dict[int, edgeData]] = dict()
        for key in self.nodes_graph:
            print(key)
            print(self.nodes_graph[key].weight)
        for key in self.edges_graph.get(id1):
            x = self.edges_graph.get(id1)[key].src
            if x is id1:
                temp.__setitem__(id1, x)
        return temp

    def all_out_edges_of_node(self, id1: int) -> dict:
        temp: Dict[int, Dict[int, edgeData]] = dict()
        for key in self.nodes_graph:
            print(key)
            print(self.nodes_graph[key].weight)
        for key in self.edges_graph.get(id1):
            x = self.edges_graph.get(id1)[key].src
            if x is not id1:
                temp.__setitem__(id1, x)
        return temp

    def get_mc(self) -> int:
        return self.mc

    def getsrc(self, id1: int) -> dict:
       return self.nodes_graph.get(id1).src

    def getdest(self, id1: int) -> dict:
        return self.nodes_graph.get(id1).dest

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:

        if id1 not in self.nodes_graph and id2 in self.nodes_graph:
            return False
        if id1 is None and \
                id2 is None:
            return false
        if id1 == id2:
            return False
        if weight < 0:
            return False
        if self.edges_graph.get(id1).get(id2) is not None and \
                self.edges_graph.get(id1).get(id2).w == weight:
            return True
        else:
            if self.edges_graph.get(id1).get(id2) is not None and \
                    edges_graph.get(id1).get(id2).w != weight:
                self.edges_graph.get(id1).get(id2).w = weight
                self.mc += 1
            else:
                edge = edgeData(id1, id2, weight)
                self.edges_graph.get(id1).__setitem__(id2, edge)
                self.mc += 1
                self.edgeSize += 1

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes_graph:
            return False
        else:
            self.nodes_graph.__setitem__(node_id, nodeData(node_id, pos))
            self.edges_graph.__setitem__(node_id, dict())
            self.mc += 1
            return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.nodes:
            return False
            iterator = iter(self.get_src(node_id).keys())
            while True:
                n = next(iterator)
                self.remove_edge(node_id1=n, node_id2=node_id)
                iterator = iter(self.getdest(node_id).keys())

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 is not None and node_id2 is not None and \
           node_id1 in self.edges_graph and \
           node_id2 in self.edges_graph.get(node_id1):
            self.edges_graph.get(node_id1).pop(node_id2) #[int,[]]
            self.mc += 1
            self.edgeSize -= 1
            return True
        return False
