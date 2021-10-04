#Non-recursive Topological Sortings
#Python program to print topological sorting of a DAG
from collections import defaultdict
 
#Class to represent a graph
class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list) #dictionary containing adjacency List
        self.V = vertices #No. of vertices
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # neighbors lazy generator given key
    def neighbor_gen(self,v):
        for k in self.graph[v]:
            yield k
     
    # non recursive topological sort
    def nonRecursiveTopologicalSortUtil(self, v, visited,stack):
         
        # working stack contains key and the corresponding current generator
        working_stack = [(v,self.neighbor_gen(v))]
         
        while len(working_stack) > 0:
            # get last element in stack
            v, gen = working_stack[-1]
            visited[v] = True
             
            # delete it from stack
            working_stack.pop()
             
            # run through neighbor generator until its empty
            continue_flag = True
            while continue_flag:
                next_neighbor = next(gen,None)
                 
                # if generator has returned all neighbors
                if next_neighbor is None:
                    continue_flag = False
                    # Save current key into the result stack
                    stack.append(v)
                    continue
                 
                # if new neighbor push current key and neighbor into stack
                if not(visited[next_neighbor]):
                    working_stack.append((v,gen))
                    working_stack.append((next_neighbor,self.neighbor_gen(next_neighbor)))
                    continue_flag = False
             
    # The function to do Topological Sort.
    def nonRecursiveTopologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False]*self.V
         
        # result stack
        stack = []
 
        # Call the helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if not(visited[i]):
                self.nonRecursiveTopologicalSortUtil(i, visited,stack)
         # Print contents of the stack in reverse
        print(stack[::-1])
 
g= Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);
 
print("The following is a Topological Sort of the given graph")
g.nonRecursiveTopologicalSort()