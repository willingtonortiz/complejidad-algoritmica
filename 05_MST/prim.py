import math
from queue import PriorityQueue


def prim(graph):
    size = len(graph)
    visited = [False for i in range(size)]
    mst = [None for i in range(size)]
    total = 0

    mst[0] = 0
    pq = PriorityQueue()
    pq.put((0, 0, 0))

    while not pq.empty():
        w, u, v = pq.get()

        if visited[v]:
            continue
        visited[v] = True
        mst[v] = u
        total += w

        for neig, weig in graph[v]:
            if visited[neig]:
                continue
            pq.put((weig, v, neig))
    print(total)
    return mst
    


def run():
    graph = [
        [(1, 2), (2, 3), (4, 6)],
        [(0, 2), (4, 2), (5, 3)],
        [(0, 3), (3, 5), (4, 1)],
        [(2, 5), (4, 5), (5, 6)],
        [(0, 6), (1, 2), (2, 1), (3, 5), (5, 4)],
        [(3, 6), (1, 3), (4, 4)]
    ]

    mst = prim(graph)
    print(mst)

if __name__ == "__main__":
    run()