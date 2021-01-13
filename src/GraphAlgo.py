from typing import List
from src.Encoder import DiGraphEncoder
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from queue import PriorityQueue
import json
import math
import random
import matplotlib.pyplot as plt

from src.nodeData import nodeData

path = []
lists = []


class GraphAlgo(GraphAlgoInterface):
    """
     constructor
    """

    def __init__(self, graph=DiGraph()):
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
           @return: True if the save was successful, False o.w.
           """
        try:
            with open(file_name, 'w') as f:
                json.dump(self.graph, f, cls=DiGraphEncoder)
                return True
        except:
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
This function returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
Dijkstra's algorithm: An algorithm for finding the shortest paths between nodes in a graph
he gets 2 nodes- src and -dest should get from the src node to the dest node and go through the nodes with the lowest weight.
We will first initialize all the weights of the nodes to infinity so that we know which node we have not yet updated,
 and then we set a priority queue that will contain the nodes we will visit and update their weights.
Each node he visited will be marked as a visit (correct),
and that way we will know if we visited this node or not,
In the priority queue, we enter the first node and initialize its weight to 0
 For the current junction,we will include all its neighbors and update their temporary weights.
The weight of each node is updated according to the parent weight of that node plus the temporary distance between them which is the weight on the edge.
Then the same node we started with becomes the father of this node and leaves the queue,
it is marked as one we have already visited and we will not return to it again.
Each of the introduced neighbors treats him the same way:
 putting his neighbors in line and updating their weights.
so if one of the neighbors is already updated with weight because we reached it through another father-node,
then we will check through which neighbor that node will have the lowest weight, then we will keep the lower weight.
We will take the node out of the queue and return it with the updated weight.
To the same junction is also updated the new father through which we reached a junction with a lower weight.
And so for each node up to the node, we set to reach in the graph.
	 * @param id1
	 * @param id2
	 * This function uses the Dijkstra's algorithm to find the shortest path between id1 and id2
	 *@return The distance of the path, a list of the nodes ids that the path goes through
          """
        if id1 not in self.graph.get_all_v() or id2 not in self.graph.get_all_v():
            return (math.inf, [])
        if id1 is id2:
            return (0, [id1])  # bdika
        # init all varibales in node
        self.__init_all()
        q = PriorityQueue()
        node = self.graph.get_all_v()[id1]
        node.weight = 0
        q.put((node.weight, node))

        while not q.empty():
            v = q.get()[1]
            for edge in self.graph.all_out_edges_of_node(v.getId()).values():
                u = self.graph.get_all_v()[edge.get_dest()]
                dist = edge.get_w() + v.weight
                if dist < u.weight:
                    u.weight = dist
                    u.info = v.getId()
                    q.put((u.weight, u))
        path = []
        dest = self.graph.get_all_v()[id2]
        if dest.weight is math.inf:
            return (math.inf, [])
        path.append(dest.getId())
        str = dest.info
        while str != "":
            node = self.graph.get_all_v()[str]
            path.insert(0, node.getId())
            str = node.info
        return dest.weight, path

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
        global path, lists

        path = []
        lists = []

        self.__tarjan(id1)
        return path

    # Tarjan's algorithm, iterative version.
    def __tarjan(self, v: int):
        """" This algorithm is iterative constructed.
It does go through a weighted directed graph on the node stack that starts empty and stores the history of the nodes that have been
 explored but are not yet committed to a tightly connected component.
As nodes made distributed when the search returns up the tree;
They only pop up when a well-connected whole component is found.
The outermost loop searches each node that has not yet been visited, and makes sure that the nodes made accessible,
from the first node still passing through.
Find all the heirs from the node_at node, and report all the well-connected components of the same sub-graph.
When each node finishes returning, if its low link is still set to its index,
So this is the root node of a tightly connected component, created by all the nodes above it in the stack.
The algorithm raises the pile to the current node and includes it, displaying all of these nodes as a tightly connected component.
That is, each binding element is marked by the same id of the parent vertex of that binding element,
and then the binding elements marked in the graph are returned, or of a particular vertex -
return the path of its binding element or the list of all the binding elements in the graph.
It serves us as a solution to 2 functions:
Connected_component
Connected_components
      @ returns - dictionary of all scc
      """
        global path, lists
        stack = []
        id = 0
        work = [(v, 0)]  # NEW: Recursion stack.
        while work:
            v, i = work[-1]  # i is next successor to process.
            del work[-1]
            node_at: nodeData = self.graph.get_all_v().get(v)
            if i == 0:  # When first visiting a vertex:
                stack.append(v)
                id += 1
                node_at.weight = id
                node_at.tag = id
                node_at.info = "true"
            recurse = False
            j = 0
            for w, edge in self.graph.all_out_edges_of_node(v).items():
                to: nodeData = self.graph.get_all_v().get(w)
                if to.tag == 0:
                    work.append((v, j + 1))
                    work.append((w, 0))
                    recurse = True
                    j += 1
                    break
                elif to.info == "true":
                    j += 1
                    node_at.weight = min(node_at.weight, to.weight)
            if recurse:
                continue  # NEW
            if node_at.tag == node_at.weight:
                path = []
                while stack:
                    w = stack.pop()
                    node = self.graph.get_all_v().get(w)
                    node.info = "false"
                    node.weight = node_at.tag
                    path.insert(0, w)
                    if v == w:
                        break
                lists.insert(0, path)
            if work:  # NEW: v was recursively visited.
                w = v
                v, _ = work[-1]
                to = self.graph.get_all_v().get(w)
                node_at.weight = min(node_at.weight, to.weight)

    def connected_components(self) -> List[list]:
        """
              Finds all the Strongly Connected Component(SCC) in the graph.
              @return: The list all SCC
              """
        if self.graph is None:
            return [[]]
        self.__init_all()
        global path, lists
        stack = []
        lists = []
        for node in self.graph.get_all_v().values():
            if node.tag == 0:
                self.__tarjan(node.getId())
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
                          (y2_coordinate - y1_coordinate), length_includes_head=True, width=0.00001,
                          head_width=0.00032, color='black')
        plt.ylabel("y axis")
        plt.title("OOP_Ex3")
        plt.xlabel("x axis")
        plt.title("My Graph")
        plt.show()
