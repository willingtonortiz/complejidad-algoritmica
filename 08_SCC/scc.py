
def toposort(graph):
    size = len(graph)
    visited = [False for i in range(size)]
    stack = []

    def dfs(node):
        if visited[node]:
            return
        visited[node] = True

        for jdx in graph[node]:
            if visited[jdx]:
                return
            dfs(jdx)
        stack.insert(0, node)

    for i in range(size):
        dfs(i)
    return stack


def reverse_graph(graph):
    size = len(graph)
    rgraph = [[] for i in range(size)]
    for (idx, node) in enumerate(graph):
        for jdx in node:
            rgraph[jdx].append(idx)
    return rgraph


def scc(graph):
    size = len(graph)
    topo = toposort(graph)
    rgraph = reverse_graph(graph)

    index = -1
    visited = [False for i in range(size)]
    scc = []

    def dfs(node, index):
        if visited[node]:
            return
        visited[node] = True
        scc[index].append(node)

        for jdx in rgraph[node]:
            if visited[jdx]:
                return
            dfs(jdx, index)
    
    while len(topo) > 0:
        start = topo.pop(0)
        if visited[start]:
            continue
        else:
            index += 1
            scc.append([])
            dfs(start, index)
    
    for row in scc:
        print(row)


def run():
    graph = [
        [2, 3],
        [0],
        [1],
        [4],
        []
    ]
    # graph = [
    #     [1],
    #     [2],
    #     [3, 4],
    #     [0],
    #     [2]
    # ]
    scc(graph)


if __name__ == "__main__":
    run()