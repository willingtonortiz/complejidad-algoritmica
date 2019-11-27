import math

def floyd_warshall(graph):
    size = len(graph)

    dist = [[graph[i][j] if graph[i][j] != None else math.inf for j in range(size)] for i in range(size)]

    for k in range(size):
        for i in range(size):
            for j in range(size):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist


def run():
    graph = [
        [0, 50, 30, 100, 10],
        [50, 0, 5, 20, None],
        [30, 5, 0, 50, None],
        [100, 20, 50, 0, 10],
        [10, None, None, 10, 0]
    ]

    dist = floyd_warshall(graph)
    print("")
    for row in dist:
        print(row)


if __name__ == "__main__":
    run()