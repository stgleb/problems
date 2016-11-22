from python.graphs import graph


def bfs(root, graph):
    q = [root]
    visited = {root}

    while len(q):
        cur = q[0]
        q = q[1:]

        for v in graph[cur]:
            if v not in visited:
                q.append(v)
                visited.add(v)

    return visited


def find_new_root(all_visited, graph):
    for v in graph:
        if v not in all_visited:
            return v

    return None


def connected_components(graph):
    all_visited = set()
    component_count = 0
    components = dict()

    while len(all_visited) < len(graph.keys()):
        root = find_new_root(all_visited, graph)
        visited = bfs(root, graph)
        all_visited = all_visited | visited
        component_count += 1
        components[component_count] = list(visited)

    return components


if __name__ == "__main__":
    graph[4] = [4, 5]
    graph[5] = [6]
    graph[6] = [5]
    graph[7] = []

    print(connected_components(graph))
