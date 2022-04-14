from collections import defaultdict


# Depth First Search (DFS) Algorithm
class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v)

        for n in self.graph[v]:
            if n not in visited:
                self.DFSUtil(n, visited)


    def DFS(self, v):

        visited = set()

        self.DFSUtil(v, visited)



if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.DFS(2)
