from edgeData import edgeData
from DiGraph import DiGraph
if __name__ == '__main__':
   edge=edgeData(0,1,500)
   edge.info="23112312"
   print(edge.getSrc())
   print(edge.info)
   print(edge)
   pos= (7,8)

   g= DiGraph()
   print("************")
   print(g.add_node(0,pos))
   print(g.add_node(0, pos))
   print(g.add_node(1, pos))
   print(g.add_node(2, pos))
   print("************")
   print(g.add_edge(0,2,500))
   print(g.add_edge(1,0,500))
   print(g.add_edge(0,1,300))
   print(g.add_edge(2,0,500))
   print("********mc edges vertexs******")
   print(g.v_size())
   print(g.get_mc())
   print(g.e_size())
   print("**************")
   print("******all_out_edges_of_node******")
   dict=g.all_out_edges_of_node(0)
   for x in dict:
       print(x,dict[x])
   print("******all_in_edges_of_node******")

   dict1=g.all_in_edges_of_node(0)
   for x in dict1:
       print(x,dict1[x])
   print("************")
   print("*****remove node*******")
   g.remove_node(0)
   print(g.v_size())
   print(g.get_mc())
   print(g.e_size())
   print("******all_out_edges_of_node******")
   dict=g.all_out_edges_of_node(0)
   for x in dict:
       print(x,dict[x])
   print("******all_in_edges_of_node******")
   dict1=g.all_in_edges_of_node(0)
   for x in dict1:
       print(x,dict1[x])
   print("************")
   print(g.remove_edge(0,2))
   print(g.remove_edge(1,0))
   print(g.remove_edge(0, 1))
   print(g.remove_edge(0, 1))
