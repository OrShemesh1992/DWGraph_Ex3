from typing import List
from Encoder import DiGraphEncoder
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from queue import PriorityQueue
import json
import math
class GraphAlgo(GraphAlgoInterface):
    def __init__(self,graph:DiGraph):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, 'r') as f:
                s = json.load(f)
            g = DiGraph()
            for node in s["Nodes"]:
                if "pos" in node:
                    pos = tuple(map(float, str(node["pos"]).split(",")))
                    g.add_node(node['id'], pos)
                else:
                    g.add_node(node['id'])

            for edge in s["Edges"]:
                g.add_edge(edge["src"], edge["dest"], edge["w"])
            self.graph = g
            return True
        except Exception as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, 'w') as f:
                json.dump(self.graph, f, cls=DiGraphEncoder)
                return True
        except:
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
         if id1 not in self.graph.get_all_v() or id2 not in self.graph.get_all_v():
             return (-1,[])
         if id1 is id2:
             return (0,[id1]) # bdika
         #init all varibales in node
         self.init_all()
         q=PriorityQueue()
         node=self.graph.get_all_v()[id1]
         node.weight = 0
         q.put((node.weight , node))

         while not q.empty():
             v=q.get()[1]
             for edge in self.graph.all_out_edges_of_node(v.getId()).values():
                 u= self.graph.get_all_v()[edge.getDest()]
                 dist = edge.getW()+v.weight
                 if dist < u.weight:
                     u.weight=dist
                     u.info=v.getId()
                     q.put((u.weight,u))
         path = []
         dest = self.graph.get_all_v()[id2]
         if dest.weight is math.inf:
             return  (-1,[])
         path.append(dest.getId())
         str = dest.info
         while str != "":
             node = self.graph.get_all_v()[str]
             path.insert(0, node.getId())
             str = node.info
         return dest.weight,path

    def init_all(self):
        for node in self.graph.get_all_v().values():
            node.weight=math.inf
            node.tag=0
            node.info=""

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        pass