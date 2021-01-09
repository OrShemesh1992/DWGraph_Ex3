# DWGraph_Ex3

## The purpose of the project:
Building a directed weighted graph system that builds a weighted and directed graph.
This project was the last part in building directed and weighted graphs.
In the previous project we created a Pokemon game based on a deliberate and weighted graph in the Java language.

 in this project we learned to build a directed and weighted graph in the Python programming language, we learned to make the differences in writing the functions and algorithms between the different languages,
And we have created similar classes and algorithms in order to make comparisons between projects and runtimes between different functions.

- On the wiki pages can not see the comparison between the graphs, functions and runtimes of the 2 projects.

# We have created different classes:
## classes:

### nodeData: 
In this class we have implemented operations at a node (vertex) in a weighted graph (directional).
id, location, weight, tag of each vertex. 

### edgeData:
In this class we performed operations on the edges of the graph.
Each edge consists of 2 nodes - src and dest and each edgee has a weight.

### DiGraph:
In this class we created a connection between neighboring vertices by sides to get at the end of a graph, we built different functions,
And we created a hashap that contains all the vertices of the graph,
In addition, we have created a hashmap within a hashap that first contains the nodes in the graph and each node has the hashmap that contains the list of neighbors - the ribs to which they are attached along with the weight of each edge.

### The various functions in this class:

|         Name       |    Description   |                                                                                                                                 
| ------------------ | ----------------       |
|  v_size            |  In this class we implemented operations at a node (vertex) in a weighted(directional) graph. (Location, weight of each node) |                                    
| e_size             | In this class we performed operations on the ribs in a rib graph composed of src and dest and it has weight.                  |  
|  get_all_v         |  In this class we implemented operations at a node (vertex) in a weighted(directional) graph. (Location, weight of each node) |                                    
|  all_in_edges_of_node          | In this class we performed operations on the ribs in a rib graph composed of src and dest and it has weight.                  |  
|  all_out_edges_of_node            |  In this class we implemented operations at a node (vertex) in a weighted(directional) graph. (Location, weight of each node) |                                    
| get_mc          | In this class we performed operations on the ribs in a rib graph composed of src and dest and it has weight.                  |  
|  add_edge          |  In this class we implemented operations at a node (vertex) in a weighted(directional) graph. (Location, weight of each node) |          
| add_node            |  In this class we implemented operations at a node (vertex) in a weighted(directional) graph. (Location, weight of each node) |                              
| remove_node         | In this class we performed operations on the ribs in a rib graph composed of src and dest and it has weight.                  |  
|  remove_edge          |  In this class we implemented operations at a node (vertex) in a weighted(directional) graph. (Location, weight of each node) |          


