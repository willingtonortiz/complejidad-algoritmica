
 

def topo_sort(graph, begin):
    glob = [0, 0]
    size = len(graph)
    ds = [None] * size
    fs = [None] * size
    stack = []

    def dfs(vertex):
        if ds[vertex] != None:
            return
        ds[vertex] = glob[0]
        glob[0] += 1
        # stack.append(vertex)
        
        for neig in graph[vertex]:
            if ds[neig] == None:
                dfs(neig)
        
        stack.append(vertex)
    
    for i in range(size):
        dfs(i)
    return list(reversed(stack))


def run():
    graph = [
        [2],
        [2],
        [4, 6],
        [5, 7],
        [],
        [],
        [7],
        []
    ]
    
    temp = topo_sort(graph, 0)

    print(temp)



if __name__ == "__main__":
    run()
