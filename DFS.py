from collections import defaultdict


# Depth First Search (DFS) Algorithm
class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def visit(self, v, visited):
        visited.add(v)
        print(v)

        for n in self.graph[v]:
            if n not in visited:
                self.visit(n, visited)


    def dfs(self, v):

        visited = set()

        self.visit(v, visited)



if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.dfs(2)



# marked = [False] * len(arr)
# def depth_first_search(G, v):
#     visit(v)
#     marked[v] = True

#     for u in G.neighbors(v):
#         if not marked[u]:
#             depth_first_search(G, u)

# # marked = [False] * len(arr)
# def dfs_iter(G, v):
#     stack = [v]

#     while len(stack) > 0:
#         v = stack.pop()
#         if not marked[u]:
#             visit(v)
#             marked[v] = True
            
#             for u in G.neighbors(v):
#                 if not marked[u]:
#                     stack.append(u)

