"""
Dijkstra algorithm finding min paths from root to all other vertexes.
"""

from heapq import heappop as pop
from heapq import heappush as push


def dijkstra_naive(root, graph):
    q = [root]
    visited = set()
    path = [v for v in graph.keys()]
    min_path = [1 << 32 for _ in range(len(graph))]
    min_path[root] = 0

    while q:
        cur = q[0]
        q = q[1:]

        if cur not in visited:
            for v in range(len(graph[cur])):
                if v != cur and graph[cur][v] >= 0 and min_path[cur] + graph[cur][v] < min_path[v]:
                    min_path[v] = min_path[cur] + graph[cur][v]
                    path[v] = cur
                q.append(v)

        visited.add(cur)

    return min_path, path


def dijkstra_optimal(root, graph):
    q = [(0, root)]
    visited = set()
    path = [v for v in graph.keys()]
    min_path = [1 << 32 for _ in range(len(graph))]
    min_path[root] = 0

    while q:
        _, cur = pop(q)

        if cur not in visited:
            for v in range(len(graph[cur])):
                if v != cur and graph[cur][v] >= 0 and min_path[cur] + graph[cur][v] < min_path[v]:
                    min_path[v] = min_path[cur] + graph[cur][v]
                    path[v] = cur
                push(q, (min_path[v], v))

        visited.add(cur)

    return min_path, path


if __name__ == "__main__":
    graph = {
        0: [-1, 1, 3, -1],
        1: [2, -1, 1, 4],
        2: [3, 1, -1, 1],
        3: [-1, 4, 1, -1]
    }
    print(dijkstra_naive(0, graph))
    print(dijkstra_optimal(0, graph))
