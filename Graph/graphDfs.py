def dfs(graph,sn,visited=None):
    if visited is None:
        visited = set()
    
    visited.add(sn)
    print(sn, end=" ")

    for neighbour in graph[sn]:
        if neighbour not in visited:
            dfs(graph,neighbour,visited)
vertex = int(input("Enter the vertex: "))
edge = int(input("Enter the edges: "))
adjList = [[] for _ in range(vertex)]

for i in range(edge):
    v1, v2 = map(int,input().split())
    adjList[v1].append(v2)
    adjList[v2].append(v1)

sn = int(input("Enter the Starting Vertex: "))
dfs(adjList,sn)