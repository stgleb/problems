from python.graphs import graph


def dfs(root, graph):
    stack = [root]
    visited = set(stack)

    while len(stack):
        cur = stack.pop()
        print(cur)

        for v in graph[cur]:
            if v not in visited:
                stack.append(v)
                visited.add(v)
                break


def dfs_recursive(root, graph, visited):
    print(root)
    visited.add(root)

    for v in graph[root]:
        if v not in visited:
            dfs_recursive(v, graph, visited)


if __name__ == "__main__":
    print("Start from 0")
    dfs(0, graph)
    print("Start from 2")
    dfs(2, graph)
    print("Start from 3")
    dfs_recursive(3, graph, {3})
