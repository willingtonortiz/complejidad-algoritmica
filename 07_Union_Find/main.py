import math

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


def run():
    size, rela, queries = map(int, input().split(" "))
    uf = WQUPC(size)

    for i in range(rela):
        a, b = map(lambda x: ord(x) - 97, input().split(" "))
        uf.union_sets(a, b)

    for i in range(queries):
        a, b = map(lambda x: ord(x) - 97, input().split(" "))
        print(uf.is_same_set(a, b))


if __name__ == "__main__":
    run()

