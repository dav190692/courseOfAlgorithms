import queue



class Graph:
    def __init__(self, gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict


    def addVertex(self, vertex):
        if vertex not in self.gdict.keys():
            self.gdict[vertex] = []
            return True
        return False
    

    def addEdge(self, vertex1, vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys() :
            self.gdict[vertex1].append(vertex2)
            self.gdict[vertex2].append(vertex1)
            return True
        return False
    

    def removeEdge(self, v1, v2):
        if v1 in self.gdict.keys() and v2 in self.gdict.keys():
            try:
                self.gdict[v1].remove(v2)
                self.gdict[v2].remove(v1)
            except ValueError:
                pass    
            return True
        return False
    

    def removeVertex(self, vertex):
        if vertex in self.gdict.keys():
            for i in self.gdict[vertex]:
                self.gdict[i].remove(vertex)
            del self.gdict[vertex]
            return True
        return False
    


    def print_graph(self):
        for vertex in self.gdict:
            print(vertex, ':', self.gdict[vertex])


    def bfs(self, vertex):
        visited = set()
        visited.add(vertex)
        temp_queue = queue.Queue()
        temp_queue.put(vertex)
        while temp_queue:
            current_vertex = temp_queue.get()
            print(current_vertex)
            for adjacent_vertex in self.gdict[current_vertex]:
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    temp_queue.put(adjacent_vertex)


    def dfs(self, vertex):
        visited = set()
        temp_stack = stack.linkedList.Stack()
        temp_stack.push(vertex)
        while temp_stack:
            current_vertex = temp_stack.pop()
            print(current_vertex)
            if current_vertex not in visited:
                visited.add(current_vertex)
            for adjacent_vertex in self.gdict[current_vertex]:
                if adjacent_vertex  not in visited:
                    temp_stack.push(adjacent_vertex)



                
        




custom_graph = Graph()


custom_graph.addVertex('A')
custom_graph.addVertex('B')
custom_graph.addVertex('C')
custom_graph.addVertex('D')
custom_graph.addVertex('E')



custom_graph.addEdge('A', 'B')
custom_graph.addEdge('A', 'C')
custom_graph.addEdge('B', 'E')
custom_graph.addEdge('C', 'D')
custom_graph.addEdge('E', 'D')





# custom_graph.removeEdge('A', 'B')

# custom_graph.removeVertex('B')



custom_graph.print_graph()

custom_graph.dfs('A')


    





