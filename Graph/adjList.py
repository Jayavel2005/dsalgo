class Graph:
    def __init__(self,vertex) -> None:
        self.adjList = [[] for i in range(vertex)]

    def insert(self,v1,v2):
        self.adjList[v1].append(v2)
        self.adjList[v2].append(v1)

    def bfs(self, src):
        visited = set()
        queue = [src]
        visited.add(src)

        while queue:
            node = queue.pop(0)
            print(node,end=" -> ")

            for nei in self.adjList[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)

    def display(self):
        for i in range(len(self.adjList)):
            print(f"{i}:{self.adjList[i]}")

vertex = int(input("Enter the No.of Vertex: "))
edges = int(input("Enter the Number of edges: "))

graph = Graph(vertex)
for _ in range(edges):
    v1, v2 = map(int, input().split())
    graph.insert(v1,v2)
graph.display()
graph.bfs(0)