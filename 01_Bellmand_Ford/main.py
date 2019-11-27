import math


def bellman_ford(graph, source):
    size = len(graph)

    path = [None for i in range(size)]
    path[source] = None
    weights = [math.inf for i in range(size)]
    weights[source] = 0

    for i in range(size - 1):
        for (idx, node) in enumerate(graph):
            for jdx, weig in node:
                if weights[jdx] > weights[idx] + weig:
                    weights[jdx] = weights[idx] + weig
    
    for (idx, node) in enumerate(graph):
        for jdx, weig in node:
            if weights[jdx] > weights[idx] + weig:
                print("CICLO NEGATIVO => GG")
    
    return weights, path


def run():
    s, t, y, x, z = 0, 1, 2, 3, 4
    graph = [
        [(t, 6), (y, 7)],
        [(y, 8), (z, -4), (x, 5)],
        [(x, -3), (z, 9)],
        [(t, -2), (z, 7)],
        [(s, 2)]
    ]

    dist, path = bellman_ford(graph, 0)
    print(dist)


if __name__ == "__main__":
    run()