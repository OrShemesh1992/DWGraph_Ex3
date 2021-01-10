from typing import List
from Encoder import DiGraphEncoder
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from queue import PriorityQueue
import json
import math
import random
import matplotlib.pyplot as plt


stack = []
id = 0
sccCount = 0
path = []
lists=[]

class GraphAlgo(GraphAlgoInterface):
    """
     constructor
    """
    def __init__(self, graph= DiGraph()):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        """
              :return: the directed graph on which the algorithm works on.
              """
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        """
            Loads a graph from a json file.
            @param file_name: The path to the json file
            @returns True if the loading was successful, False o.w.
            """
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
        """
           Saves the graph in JSON format to a file
           @param file_name: The path to the out file
           @return: True if the save was successful, Flase o.w.
           """
        try:
            with open(file_name, 'w') as f:
                json.dump(self.graph, f, cls=DiGraphEncoder)
                return True
        except:
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
         """
            Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
            @param id1: The start node id
            @param id2: The end node id
            @return: The distance of the path, the path as a list
            Dijkstra's algorithm: An algorithm for finding the shortest paths between nodes in a graph
            he gets 2 nodes- src and -dest should get from the src node to the dest node and go through the nodes with the lowest weight.
            We will first initialize all the weights of the nodes to infinity so that we know which node we have not yet updated,
            and then we set a priority queue that will contain the nodes we will visit and update their weights.
            In addition, we set the Hashmap to initialize all nodes in false.
            Each node he visited will be marked as a visit (correct),
            and that way we will know if we visited this node or not,
            and finally, if there is such a node, then he is not connected to the other node and he will remain marked as false.
            .
            In the priority queue, we enter the first node and initialize its weight to 0,
            and all the other nodes in the graph are initialized to infinity.
            For the current junction,we will include all its neighbors and update their temporary weights.
            The weight of each node is updated according to the parent weight of that node plus the temporary distance between them which is the weight on the edge.
            Then the same node we started with becomes the father of this node and leaves the queue,
            it is marked as one we have already visited and we will not return to it again.
            Each of the introduced neighbors treats him the same way:
            putting his neighbors in line and updating their weights.
            so if one of the neighbors is already updated with weight because we reached it through another father-node, then we will check through which neighbor that node will have the lowest weight, then we will keep the lower weight. We will take the node out of the queue and return it with the updated weight. To the same junction is also updated the new father through which we reached a junction with a lower weight.
            And so for each node up to the node, we set to reach in the graph.

         """
         if id1 not in self.graph.get_all_v() or id2 not in self.graph.get_all_v():
             return (math.inf,[])
         if id1 is id2:
             return (0, [id1]) # bdika
         #init all varibales in node
         self.__init_all()
         q = PriorityQueue()
         node = self.graph.get_all_v()[id1]
         node.weight = 0
         q.put((node.weight, node))

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
             return  (math.inf,[])
         path.append(dest.getId())
         str = dest.info
         while str != "":
             node = self.graph.get_all_v()[str]
             path.insert(0, node.getId())
             str = node.info
         return dest.weight,path

    def __init_all(self):
        """
         Initialize all the nodes
        """
        for node in self.graph.get_all_v().values():
            node.weight = math.inf
            node.tag = 0
            node.info = ""



    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        """
        if self.graph is None or id1 not in self.graph.get_all_v():
            return []
        self.__init_all()
        global stack,id,sccCount
        stack=[]
        id=0
        sccCount=0
        self.__dfs(id1)
        return path

    def __dfs(self,id1:int):
        """
        tarjan algorithm:
        First depth search (DFS) starts from a node that receives from the isConnected function
        (passes over nodedata) the nodes are located on a stack in the order of their visit.
        When the first depth search recursively visits the at node and its descendants,
        those nodes do not necessarily suck out of the pile when this recursive call returns.
        the essential unchanging characteristic is that a node remains in a stack after its visit if and only if there is a path
        in the input graph from it to any node earlier in the stack.
        In other words, in DFS a junction is removed from the stack only after crossing all of its connected paths.
        When the DFS goes back it will remove the nodes in a single path and return to the root to start a new path.
        At the end of the conversation that criticizes at and his descendants,
        we know if at itself has a path to each node earlier in the stack.
        If so, the call repeats, leaving the at in the stack to keep the variable. If not, then at must be the root of its strongly connected component,
        consisting of at along with later nodes in a stack of at (such nodes have paths back to at, but not to any previous node,
        because if they had paths to previous nodes So at will also have paths to previous nodes and that's a lie).
        The connected component rooted in at node from the stack and is returned, retaining the variable again
	    @param id1: from the function connected_component -is a node from node data
        """
        global stack,id,sccCount,path,lists
        # on stack - info , ids - tag, low -weight per node.
        stack.append(id1)
        at=self.graph.get_all_v()[id1]
        id+=1
        at.tag=id
        at.weight=id
        at.info="true"

        for id2 in self.graph.all_out_edges_of_node(id1):
            to = self.graph.get_all_v()[id2]
            if to.tag == 0 : self.__dfs(to.getId())
            if to.info == "true": at.weight=min(at.weight,to.weight)


        if at.tag == at.weight:
            path=[]
            while stack:
                id_get = stack.pop()
                node = self.graph.get_all_v()[id_get]
                node.info="false"
                node.weight=at.tag
                path.insert(0, id_get)
                if node.getId() is at.getId() :
                    break
            lists.insert(0,path)
            sccCount+=1

    def connected_components(self) -> List[list]:
        """
              Finds all the Strongly Connected Component(SCC) in the graph.
              @return: The list all SCC
              """
        if self.graph is None :
            return [[]]
        self.__init_all()
        global stack, id, sccCount, path,lists
        stack = []
        id = 0
        sccCount = 0
        lists=[]
        for node in self.graph.get_all_v().values():
            if node.tag == 0:
                self.__dfs(node.getId())
        return lists


    def plot_graph(self) -> None:
        """
            Plots the graph.
            If the nodes have a position, the nodes will be placed there.
            Otherwise, they will be placed in a random but elegant manner.
            @return: None
            """
        all_nodes = self.graph.get_all_v()
        x = []
        y = []
        for i in all_nodes.values():
            if i.getPos():
                x.append(i.getPos()[0])
                y.append(i.getPos()[1])
            else:
                x_random = random.uniform(35.18, 35.2)
                y_random = random.uniform(32.1, 32.2)
                i.setPos((x_random, y_random, 0.0))
                x.append(x_random)
                y.append(y_random)
        n = [j for j in all_nodes.keys()]
        fig, ax = plt.subplots()
        ax.scatter(x, y)
        for p, txt in enumerate(n):
            ax.annotate(n[p], (x[p], y[p]))
        plt.plot(x, y, "black")
        for i in all_nodes.keys():
            for j in self.graph.all_out_edges_of_node(i):
                x1_coordinate = all_nodes.get(i).getPos()[0]
                y1_coordinate = all_nodes.get(i).getPos()[1]
                x2_coordinate = all_nodes.get(j).getPos()[0]
                y2_coordinate = all_nodes.get(j).getPos()[1]
                plt.arrow(x1_coordinate, y1_coordinate, (x2_coordinate - x1_coordinate),
                          (y2_coordinate - y1_coordinate), length_includes_head=True, width=0.000010,
                          head_width=0.00006, color='black')
        plt.ylabel("y axis")
        plt.title("OOP_Ex3")
        plt.xlabel("x axis")
        plt.title("My Graph")
        plt.show()
