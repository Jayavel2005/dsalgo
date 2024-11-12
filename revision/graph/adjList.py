class Graph:
    def __init__(self, vertices):
        self.adjList = [[] for i in range(vertices)]

    def insert(self, u, v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)

    def display(self):
        for i in range(len(self.adjList)):
            print(f"{i} : {self.adjList[i]}")


vertex = int(input("Enter the No.of Vertex: "))
edges = int(input("Enter the Number of edges: "))

graph = Graph(vertex)
for _ in range(edges):
    v1, v2 = map(int, input().split())
    graph.insert(v1,v2)
graph.display()