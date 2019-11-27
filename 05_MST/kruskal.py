import math
from queue import PriorityQueue

class WQUPC():
    def __init__(self, size):
        self.initialize(size)
    
    def initialize(self, size):
        self.rank = [i for i in range(size)]
        self.parent = [i for i in range(size)]

    def find_set(self, u):
        if u == self.parent[u]:
            return u
        self.parent[u] = self.find_set(self.parent[u])
        return self.parent[u]
    
    def union_sets(self, u, v):
        u = self.find_set(u)
        v = self.find_set(v)

        if u == v:
            return

        if self.rank[u] > self.rank[v]:
            self.parent[v] = u
        elif self.rank[u] > self.rank[v]:
            self.parent[u] = v
        else:
            self.parent[u] = v
            self.rank[v] += 1
        
    def is_same_set(self, u, v):
        u = self.find_set(u)
        v = self.find_set(v)

        return u == v


def kruskal(graph):
    size = len(graph)
    count = 1
    pq = PriorityQueue()
    uf = WQUPC(size)
    mst = []

    for (idx, node) in enumerate(graph):
        for neig, weig in node:
            pq.put((weig, idx, neig))
    
    while count < size and not pq.empty():
        weig, start, end = pq.get()

        if uf.is_same_set(start, end):
            continue
        uf.union_sets(start, end)
        mst.append((weig, start, end))

        count += 1
    
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

    mst = kruskal(graph)
    print(mst)


if __name__ == "__main__":
    run()