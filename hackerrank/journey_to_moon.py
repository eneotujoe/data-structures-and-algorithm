from collections import defaultdict


def journey_to_moon(n, astronaut):
    graph = defaultdict(list)

    for u, v in astronaut:
        graph[u].append(v)
        graph[v].append(u)
    print(graph)

    visited = [False] * n
    valid_pairs = n * (n-1) // 2

    for v in range(n):
        if visited[v] == False:
            num_persons = dfs(v, graph, visited)
            valid_pairs -= num_persons * (num_persons - 1) // 2

    return valid_pairs

def dfs(u, graph, visited):
    visited[u] = True
    vertices = 1
    for v in graph[u]:
        if visited[v] == False:
            visited[v] = True
            vertices += dfs(v, graph, visited)
    return vertices


if __name__ == '__main__':
   astronaut = [
       [0, 1],
       [2, 3],
       [0, 4],
   ]
   print(journey_to_moon(5, astronaut))