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
        """
             Returns the number of vertices in this graph
             @return: The number of vertices in this graph
             """
        return len(self.__nodes_graph)

    def e_size(self) -> int:
        """
            Returns the number of edges in this graph
            @return: The number of edges in this graph
            """
        return self.__edgeSize

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using apair  (key, node_data)
              """
        return self.__nodes_graph

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
              each node is represented using a pair (key, weight)
               """
        edges_graph: Dict[int, edgeData] = dict()
        count_in = 0
        for i in self.__nodes_graph:
            if id1 in self.__edges_graph.get(i):
                edges_graph.__setitem__(i, self.__edges_graph.get(i)[id1])
                count_in += 1
        return edges_graph

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair (key,
               weight)
               """
        edges_graph: Dict[int, edgeData] = dict()
        count_out = 0
        if id1 in self.__nodes_graph:
            for temp in self.__edges_graph.get(id1):
                # print("key:",temp,"value: " ,self.edges_graph.get(id1)[temp])
                edges_graph.__setitem__(temp,self.__edges_graph.get(id1)[temp])
                count_out += 1
        return edges_graph

    def get_mc(self) -> int:
        """
               Returns the current version of this graph,
               on every change in the graph state - the MC should be increased
               @return: The current version of this graph.
               """
        return self.__mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
          Adds an edge to the graph.
          @param id1: The start node of the edge
          @param id2: The end node of the edge
          @param weight: The weight of the edge
          @return: True if the edge was added successfully, False o.w.

          Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
          """
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
        """
             Adds a node to the graph.
             @param node_id: The node ID
             @param pos: The position of the node
             @return: True if the node was added successfully, False o.w.

             Note: if the node id already exists the node will not be added
             """
        if node_id in self.__nodes_graph:
            return False
        else:
            self.__nodes_graph.__setitem__(node_id, nodeData(node_id, pos))
            self.__edges_graph.__setitem__(node_id, dict())
            self.__mc += 1
            return True

    def remove_node(self, node_id: int) -> bool:
        """
             Removes a node from the graph.
             @param node_id: The node ID
             @return: True if the node was removed successfully, False o.w.

             Note: if the node id does not exists the function will do nothing
             """
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
        """
            Removes an edge from the graph.
            @param node_id1: The start node of the edge
            @param node_id2: The end node of the edge
            @return: True if the edge was removed successfully, False o.w.

            Note: If such an edge does not exists the function will do nothing
            """
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

    def __repr__(self) -> str:
        _str = f"Graph: |V|={self.v_size()} , |E|={self.e_size()}\n"
        _str += "{"
        count = 0
        for nodes in self.__nodes_graph.keys():
            count += 1
            _str += f"{nodes}: {nodes}: |edges out| "
            _str += f"{len(self.all_out_edges_of_node(nodes).keys())} "
            _str += "|edges in| "
            _str += f"{len(self.all_in_edges_of_node(nodes).keys())} "
        if len(self.__nodes_graph.keys()) == count:
            _str += "}"
        else:
            _str += ", "
        return _str
