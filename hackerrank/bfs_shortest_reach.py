def bfs_shortest_reach(n, m, edges, s):
    graph = [[] for i in range(n+1)]
    edge_weight = 6
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)
    visited = [False] * (n+1)
    distances = [-1] * (n+1)
    queue = [(s, 0)]
    distances[s] = 0
    visited[s] = True

    while queue:
        u, w = queue.pop()
        for v in graph[u]:
            if visited[v] == False:
                distances[v] = w + edge_weight
                visited[v] = True
                queue.append((v, w + edge_weight))

    return distances[2:]


if __name__ == '__main__':
   edges = [
       [1, 2],
       [1, 3],
       [3, 4],
   ]
   print(bfs_shortest_reach(5, 3, edges, 1))