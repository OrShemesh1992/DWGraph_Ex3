from typing import List
from Encoder import DiGraphEncoder
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
import json


class GraphAlgo(GraphAlgoInterface):
    def __init__(self):
        self.graph = DiGraph()

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
        pass

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        pass