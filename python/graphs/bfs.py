from python.graphs import graph


def bfs(root, graph):
    q = [root]
    visited = set(q)
    print(root)

    while len(q):
        cur = q[0]
        q = q[1:]

        for v in graph[cur]:
            if v not in visited:
                visited.add(v)
                q.append(v)
                print(v)


if __name__ == "__main__":
    print("Start from 0")
    bfs(0, graph)
    print("--------------")
    print("Start from 2")
    bfs(2, graph)
