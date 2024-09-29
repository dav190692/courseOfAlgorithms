import numpy as np
from collections import deque 

class Graph:
    def __init__(self, num_vertices = 7):
        self.num_vertices = int(num_vertices)
        self.adjMatrix = np.zeros((self.num_vertices, self.num_vertices))


    def addEdge(self, src, dest):
        if (src >= 0 and src < self.num_vertices) and (dest >= 0 and dest < self.num_vertices):
            self.adjMatrix[src][dest] = 1
            self.adjMatrix[dest][src] = 1


    def dfs(self, startVertex):
        visited = self.num_vertices * [False]
        stack = deque()
        stack.append(startVertex)
        while stack:
            current_vertex = stack.pop()
            
            if not visited[current_vertex]:
                visited[current_vertex] = True
                print(current_vertex)
                # print(visited)
            for i in range(self.num_vertices):
                if self.adjMatrix[current_vertex][i] == 1 and  not visited[i]:
                    stack.append(i)


    def bfs(self, startVertex):
        visited = self.num_vertices * [False]
        queue = deque()
        queue.append(startVertex)
        visited[startVertex] = True
        while queue:
            current_vertex = queue.popleft()
            print(current_vertex)
            for i in range(self.num_vertices):
                if self.adjMatrix[current_vertex][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True













custom_graph = Graph(num_vertices=5)

custom_graph.addEdge(0, 1)
custom_graph.addEdge(0, 4)
custom_graph.addEdge(1, 2)
custom_graph.addEdge(1, 3)
custom_graph.addEdge(1, 4)
custom_graph.addEdge(2, 3)
custom_graph.addEdge(3, 4)


custom_graph.bfs(0)







print(custom_graph.adjMatrix)

