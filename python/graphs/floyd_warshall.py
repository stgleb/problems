def floyd_worshall(graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
            for k in range(len(graph)):
                if i != j and graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    return graph


if __name__ == "__main__":
    graph = {
        0: [10000, 1, 3, 10000],
        1: [2, 10000, 1, 4],
        2: [3, 1, 10000, 1],
        3: [10000, 4, 1, 10000]
    }
    print(floyd_worshall(graph))
