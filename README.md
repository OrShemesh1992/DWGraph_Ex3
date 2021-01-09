# DWGraph_Ex3

## The purpose of the project:
Building a system that builds a weighted and directed graph.
This project was the last part in building directed and weighted graphs.
In the previous project we created a Pokemon game based on a deliberate and weighted graph in the Java language.

In this project we learned to build a directed and weighted graph in the Python programming language, we learned to make the differences in writing the functions and algorithms between the different languages,
And we have created similar classes and algorithms in order to make comparisons between projects and runtimes between different functions.

- This project contains the algorithms - to find the shortest route,
Find the binding elements in the graph.
1) dijekstra- uses to find the shortest path in a directed weighted graph.
2) tarjan- uses to find the binding elements in the graph

- On the wiki pages can not see the comparison between the graphs, functions and runtimes of the 2 projects.

### The classes of the project :
### The nodeData: 
In this class we have implemented operations at a node (vertex) in a weighted graph (directional).
id, location, weight, tag of each vertex. 

### The edgeData:
In this class we performed operations on the edges of the graph.
Each edge consists of 2 nodes - src and dest and each edgee has a weight.

### The DiGraph:
- We created the hashmap within a hashmap that will contain the vertices of the graph along with their sides and weight.
The first hashmap contains the vertices that each vertex actually has the hashmap (which is the second) that contains the neighbors of their end data. That is, this side is two vertices connected together with the distance between them. And so you can reach every vertex in the graph and its neighbors.
- Connection function - add edge connected 2 neighboring vertices src and dest with the direction of the trajectory and formed a side from src to, dest together with the weight of the side which is the distance between them.
- Finally, the goal is to create a weighted and directed graph consisting of nodes and ribs connecting them. And more in this class we have created functions that add and delete nodes and ribs with their weights and with the distance between the different nodes. And functions that return the number of sides and nodes found in the chart as well as the number of operations we did in the graph. And also functions that create a collection of all vertices.

### The methods we practiced in this department:

|         Name       |    Description   |                                                                                                                                 
| ------------------ | ----------------       |
|  v_size            | number of vertices in this graph |                                    
| e_size             | number of edges in this graph                  |  
|  get_all_v         |  a dictionary of all the nodes in the Graph, each node is represented using a pair  (node_id, node_data) |                                   
|  all_in_edges_of_node          |a dictionary of all nodes connected to (to) node_id - entering it    |  
|  all_out_edges_of_node            |a dictionary of all nodes connected from node_id - exiting it    |                                    
| get_mc          | This function counts every action performed on the graph                  |  
|  add_edge          |   Adds an edge to the graph. |          
| add_node            |   Adds an node to the graph. |                              
| remove_node         | Removes a node from the graph.                 |  
|  remove_edge          |  Removes a edge from the graph. |     


### The GraphAlgo
- we used 2 algorithms:
- 1) Tarjan for checking the bond tying. The method is connected
- 2) Dijkstra - to find the shortest route in the graph, and to return the list of sides in the shortest route in the graph. In methods: shortestpathDist, shortestpath

### Using the tarjan algorithm:
- First depth search (DFS) starts from a node that receives from the isConnected function
(passes over nodedata) the nodes are located on a stack in the order of their visit.
When the first depth search recursively visits the at node and its descendants, 
those nodes do not necessarily suck out of the pile when this recursive call returns.
The essential unchanging characteristic is that a node remains in a stack after its visit if and only if there is a path
in the input graph from it to any node earlier in the stack. 
In other words, in DFS a junction is removed from the stack only after crossing all of its connected paths.
When the DFS goes back it will remove the nodes in a single path and return to the root to start a new path.
- At the end of the conversation that criticizes at and his descendants, 
we know if at itself has a path to each node earlier in the stack. 
If so, the call repeats, leaving the at in the stack to keep the variable. If not, then at must be the root of its strongly connected component,
consisting of at along with later nodes in a stack of at (such nodes have paths back to at, but not to any previous node, 
because if they had paths to previous nodes So at will also have paths to previous nodes and that's a lie).
The connected component rooted in at node from the stack and is returned, retaining the variable again

![image](https://i.ytimg.com/vi/TyWtx7q2D7Y/maxresdefault.jpg)
	
### Using the dijkstra algorithm:
It gets 2 nodes- src and dest should go from the src node to the destination node and go through the nodes with the lowest weight.
- The algorithm works as follows: 
- First we will initialize all the weights of the nodes to infinity so that we know which node we have not yet updated, 
 and then we set a priority queue that will contain the nodes we will visit and update their weights.
- In addition, we created the parentNodes shamp that will eventually contain the updated nodes through which we passed the shortest trajectory in the graph,
from the vertex src and dest.
We enter the first node and initialize its weight to 0, and all the other nodes in the graph are initialized to infinity. 
The current junction will include all of its neighbors and will update its temporary weights.
The weight of each node is updated according to the parent weight of that node plus the temporary distance between them which is the weight at the end.
Then the same junction we started with becomes the father of this junction and leaves the queue, it is already marked that we have already visited it and we will not return to it again.

- Each of the neighbors presented treats him in the same way:
Put his neighbors in line and update their weights.
Each node can have several neighbors and then also some fathers through which they come, so if one of the neighbors is already updated in weight because we reached it through another parent node, we will check through which neighbor it will be the lowest weight node, then we will keep the lower weight.
We will remove the node from the queue and return it with the updated weight.
And we will put it in the shampoo .parentNodes for the same node,
the new parent was also updated, through which we reached a node with a lower weight.
And so for each node up to the node, we set to reach the graph.

### The methods we practiced in this department:

|         Name       |    Description   |                                                                                                                                 
| ------------------ | ----------------       |
|  get_graph            | the directed graph on which the algorithm works on |                                    
|load_from_json           | Loads a graph from a json file.  |  
| save_to_json         |  Saves the graph in JSON format to a file |                                    
|  shortest_path          | shortest path from node id1 to node id2 using Dijkstra's Algorithm- return tuple of two objects (length of the path, list of nodes that are in the path)|  
|  connected_component            |Finds the Strongly Connected Component(SCC) that node id1 is a part of. |                                    
|connected_components         |Finds all the Strongly Connected Component(SCC) in the graph.  |  
| plot_graph        |Plots the graph.  If the nodes have a position, the nodes will be placed there, Otherwise, they will be placed in a random but elegant manner.|    


# in conclusion:
In this project we created a directed and weighted graph-
According to the different departments, we built a system that builds a graph from nodes that each have a unique key and sides that connect the adjacent nodes, different data structures that contain the nodes, and we added weights to each node in the graph and also distance to each side connecting 2 vertices.
We checked the shortest paths between each vertex.
And we examined all the binding components in the graph. And we used two algorithms - dijekstra and tarjan for different operations.
In addition, we used save and load to load and save the Jason-shaped graphs.
Next, we made comparisons between the 3 functions in this project in Python and the previous project in Java.

    

