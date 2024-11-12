class Graph:
    def __init__(self, vertices):
        self.graph = [[0 for i in range(vertices)]for _ in range(vertices)]
        self.vertices = vertices
    

    def adjMat(self,u,v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def display(self):
        for row in self.graph:
            print(row)
        

vertex = int(input("Enter the vertex count: "))
graph = Graph(vertex)
edges = int(input("Enter the Number of edges: "))
for i in range(edges):
    u,v = map(int,input().split())
    graph.adjMat(u,v)
    
graph.display()