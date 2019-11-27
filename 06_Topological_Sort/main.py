
def toposort(graph, start):
    size = len(graph)
    visited = [False for i in range(size)]
    stack = []

    def dfs(node):
        if visited[node]:
            return
        visited[node] = True

        for neig in graph[node]:
            if visited[neig]:
                continue
            dfs(neig)
        stack.append(node)
    
    for i in range(size):
        dfs(i)
    
    return list(reversed(stack))


def run():
    graph = [
        [1, 2],
        [3],
        [3],
        []
    ]

    path = toposort(graph, 0)
    print(path)


if __name__ == "__main__":
    run()