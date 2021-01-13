# DWGraph_Ex3
<img src="https://scontent.ftlv1-1.fna.fbcdn.net/v/t1.0-9/137204839_4245883572095318_5195765541934772574_o.jpg?_nc_cat=106&ccb=2&_nc_sid=730e14&_nc_ohc=egaAvkaxoQIAX_rWadX&_nc_ht=scontent.ftlv1-1.fna&oh=96896ac801a3f8aff5132972f90ef82e&oe=60203E5D" width="600" height="320">

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
<img src="https://scontent.ftlv5-1.fna.fbcdn.net/v/t1.0-9/138064004_4252865398063802_2532825376174938053_o.jpg?_nc_cat=102&ccb=2&_nc_sid=730e14&_nc_ohc=OFvK8R_XqHkAX_0E6X5&_nc_ht=scontent.ftlv5-1.fna&oh=d7e8e65513d636759f3e5f4b8dffa8a5&oe=60239655" width="250" height="150"> <img src="https://scontent.ftlv5-1.fna.fbcdn.net/v/t1.0-9/138187228_4252865394730469_1967892766406936052_o.jpg?_nc_cat=106&ccb=2&_nc_sid=730e14&_nc_ohc=9wwfPHYsHyAAX9m4mzc&_nc_ht=scontent.ftlv5-1.fna&oh=7d2365c26a1df9b9842fc509482e7d3a&oe=6024561B" width="250" height="150">

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
- This algorithm is iterative constructed.
It does go through a weighted directed graph on the node stack that starts empty and stores the history of the nodes that have been
 explored but are not yet committed to a tightly connected component.
As nodes made distributed when the search returns up the tree;
They only pop up when a well-connected whole component is found.
The outermost loop searches each node that has not yet been visited, and makes sure that the nodes made accessible,
from the first node still passing through.
- Find all the heirs from the node_at node, and report all the well-connected components of the same sub-graph.
When each node finishes returning, if its low link is still set to its index,
So this is the root node of a tightly connected component, created by all the nodes above it in the stack.
- The algorithm raises the pile to the current node and includes it, displaying all of these nodes as a tightly connected component.
That is, each binding element is marked by the same id of the parent vertex of that binding element,
and then the binding elements marked in the graph are returned, or of a particular vertex -
return the path of its binding element or the list of all the binding elements in the graph.
- It serves us as a solution to 2 functions:
Connected_component
Connected_components
    
### Using the dijkstra algorithm:
- Dijkstra's algorithm: An algorithm for finding the shortest paths between nodes in a graph
he gets 2 nodes- id1 and -id2 should get from the src(id1) node to the dest(id2) node and go through the nodes with the lowest weight.
- We will first initialize all the weights of the nodes to infinity so that we know which node we have not yet updated,
and then we set a priority queue that will contain the nodes we will visit and update their weights.
Each node he visited will be marked as a visit (correct), 
and that way we will know if we visited this node or not, 
- In the priority queue, we enter the first node and initialize its weight to 0
For the current junction,we will include all its neighbors and update their temporary weights.
The weight of each node is updated according to the parent weight of that node plus the temporary distance between them which is the weight on the edge.
- Then the same node we started with becomes the father of this node and leaves the queue, 
it is marked as one we have already visited and we will not return to it again. 
Each of the introduced neighbors treats him the same way:
putting his neighbors in line and updating their weights.
so if one of the neighbors is already updated with weight because we reached it through another father-node,
- then we will check through which neighbor that node will have the lowest weight, then we will keep the lower weight.
We will take the node out of the queue and return it with the updated weight. 
To the same junction is also updated the new father through which we reached a junction with a lower weight.
And so for each node up to the node, we set to reach in the graph.
  
<img src="https://programmersought.com/images/409/2b48d95d78d688f88100bd7312b6b8d1.JPEG" width="400" height="250">

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

    

