import math

def bfs(graph, start, end, path):
    size = len(graph)
    visited = [False for i in range(size)]
    queue = []
    queue.append(start)
    visited[start] = True

    while len(queue) > 0:
        idx = queue.pop(0)
        for jdx, val in enumerate(graph[idx]):
            if not visited[jdx] and val > 0:
                visited[jdx] = True
                queue.append(jdx)
                path[jdx] = idx
    return visited[end]


def ford_fulkerson(graph, start, end):
    size = len(graph)
    max_flow = 0

    # Inicializando grafos
    path = [None for i in range(size)]
    dgraph = [[0 for jdx in range(size)] for idx in range(size)]
    rgraph = [[0 for jdx in range(size)] for idx in range(size)]
    for (idx, node) in enumerate(graph):
        for jdx, weig in node:
            dgraph[idx][jdx] = weig
    
    while bfs(dgraph, start, end, path):
        path_flow = math.inf
        temp = end
        while temp != start:
            path_flow = min(path_flow, dgraph[path[temp]][temp])
            temp = path[temp]
        max_flow += path_flow

        temp = end
        while temp != start:
            fr = path[temp]
            dgraph[fr][temp] -= path_flow
            rgraph[fr][temp] += path_flow
            temp = path[temp]
    return max_flow

def run():
    graph = [
        [(1, 2), (2, 3)],
        [(3, 3)],
        [(3, 2)],
        []
    ]
    max_flow = ford_fulkerson(graph, 0, 3)
    print(max_flow)


def case_2():
    i, a, b, c, d, e, f = 0, 1, 2, 3, 4, 5, 6
    graph = [
        [(a, 6), (b, 4), (c, 1)],
        [(d, 4)],
        [(d, 1), (e, 3), (c, 3)],
        [(e, 4)],
        [(f, 4)],
        [(f, 9)],
        []
    ]

    max_flow = ford_fulkerson(graph, i, f)
    print(max_flow)


if __name__ == "__main__":
    # run()
    case_2()