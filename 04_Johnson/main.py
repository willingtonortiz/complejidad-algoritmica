import math
from queue import PriorityQueue


def bellman_fort(graph, source):
    size = len(graph)
    dist = [math.inf for i in range(size)]
    dist[source] = 0
    for k in range(size - 1):
        for (idx, node) in enumerate(graph):
            for jdx, weig in node:
                if dist[jdx] > dist[idx] + weig:
                    dist[jdx] = dist[idx] + weig
    for (idx, node) in enumerate(graph):
        for jdx, weig in node:
            if dist[jdx] > dist[idx] + weig:
                print("CICLO NEGATIVO => GG")
    return dist


def dikstra(graph, source):
    size = len(graph)
    dist = [math.inf for i in range(size)]
    visited = [False for i in range(size)]
    pq = PriorityQueue()
    dist[source] = 0
    pq.put((0, source))

    while not pq.empty():
        w, u = pq.get()
        visited[u] = True
        for jdx, weig in graph[u]:
            if visited[jdx]:
                continue
            if dist[jdx] > dist[u] + weig:
                dist[jdx] = dist[u] + weig
                pq.put((dist[jdx], jdx))
    return dist


def johnson(graph):
    # BellmanFord con el nuevo vertice
    size = len(graph)
    graph.append([])
    for i in range(size):
        graph[size].append((i, 0))
    
    dist = bellman_fort(graph, size)

    # Quitar nuevo vertice
    graph.pop()

    # Grafo primo
    gprime = [[] for i in range(size)]
    for (idx, node) in enumerate(graph):
        for jdx, weig in node:
            gprime[idx].append((jdx, weig + dist[idx] - dist[jdx]))

    # N invocaciones a dikstra
    super_path = []
    for i in range(size):
        path = dikstra(gprime, i)
        super_path.append(path)
    
    for row in super_path:
        print(row)


def run():
    w, x, y, z = 0, 1, 2, 3
    graph = [
        [(z, 2)],
        [(w, 6), (y, 3)],
        [(w, 4), (z, 5)],
        [(y, -3), (x, -7)],
    ]
    johnson(graph)


if __name__ == "__main__":
    run()