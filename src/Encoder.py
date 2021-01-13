import json
from src.DiGraph import DiGraph
from src.nodeData import nodeData


class DiGraphEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, DiGraph):
            nodeData = NodeDataEncoder()
            lists=[]
            for i in obj.get_all_v():
                for x in obj.all_in_edges_of_node(i):
                    edge=obj.all_in_edges_of_node(i)[x]
                    lists.append({"src": edge.getSrc(), "dest": edge.getDest(), "w": edge.getW()})
            return {
                'Nodes': [nodeData.default(x) for x in list(obj.get_all_v().values())],
                'Edges': [x for x in lists]
            }
        return json.JSONEncoder.default(self, obj)


class NodeDataEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, nodeData):
            if obj.getPos() is not None:
                return {
                    'id': obj.getId(),
                    'pos': obj.getPos().__str__()
                }
            else:
                return {
                    'id': obj.getId()
                }
        return json.JSONEncoder.default(self, obj)