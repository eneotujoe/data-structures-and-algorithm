import sys
from heapq import heappush, heappop
from collections import defaultdict


def dijkstra_shorttest_reach(n, edges, s):
    graph = defaultdict(list)

    for (u, v), w in edges.items():
        graph[u].append((w, v))
        graph[v].append((w, u))
    visited = [False] * (n+1)
    distance = [sys.maxsize] * (n+1)
    distance[s] = 0
    min_heap = [(distance[s], s)]

    while min_heap:
        u, w = heappop(min_heap)
        if visited[u] == True:
            continue

        visited[u] == True

        for w, v in graph[u]:
            if visited[v] == False and distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                heappush(min_heap, (distance[v], v))

    del distance[s]
    del distance[0]

    for i in range(len(distance)):
        if distance[i] == sys.maxsize:
            distance[i] = -1

    return distance


if __name__ == '__main__':
   edges = [
       [1, 2],
       [1, 3],
       [3, 4],
   ]
   print(dijkstra_shorttest_reach(5, edges, 1))