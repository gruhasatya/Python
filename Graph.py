# graph is composed of sets and edges denoted by ----------G(E,V)
# Edges ------ lines
# vertices/nodes ----- points

Null Graph --      no edges is called null graph
trival graph  --   graph having only one vertices

undirected graph and directed graph   ---- edges do not have direction  is undiredcted
                                           edges which have proper direction is directed


connected and unconnected       ----      from one node we can visit another node is call connected
                                          we cannot visit another nodes is called unconmnected

regualr graph and complete graph ---      regular in which every vertex is equal to other vertex
                                          we can visit any node from any node

cycle graph and cyclic graph    ----      graph have cycle in itself
                                          at least contains on graph

Directed acylic graph ------------------- a dircted graph that doesnot conatoin cycle
Bipartie grpah            --------        a graph in which vertex is divided into two sets



There are two ways to store graph
                                                                                    adding Edge        removing      intializing

Adjacency Matrix -------------------------- Stored in form of 2D matrix                  0(1)             0(1)           0(N*N)
Adjacency List   -------------------------- its like collection of linked list           0(1)             0(N)           0(N)









class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None]*self.V

    # function to insert edge in undirected graph

    def insert(self, source, destination):

        # Adding the node to the source node
        node = Node(destination)
        node.next = self.graph[src]
        self.graph[src] = node

        # Adding the source node to the destination
        node = Node(source)
        node.next = self.graph[destination]
        self.graph[destination] = node

    def print(self):
        for i in range(self.V)
            print("enter how many vertex/nodes{}".format(i), end=" ")
            temp = self.grpah[i]
            while temp:
                print("->{}".format(temp.data), end=" ")
                temp = temp.next
                print("\n")

if name = "__main__":
    V = 5
    graph  = Graph(V)
