import math


def diligencia_main():

    matrix = [[(2, 1), (4, 2), (3, 3)], [(7, 4), (4, 5), (6, 6)],
              [(3, 4), (2, 5), (4, 6)], [(4, 4), (1, 5), (5, 6)],
              [(1, 7), (4, 8)], [(6, 7), (3, 8)], [(3, 7), (3, 8)], [(3, 9)],
              [(4, 9)], []]

    DP = [None for i in range(10)]
    weights = [None for i in range(10)]
    DP[9] = 0

    def dp_r(start, end):

        if DP[start] != None:
            return DP[start]

        else:
            mini = math.inf

            for (weig, node) in matrix[start]:
                mini = min(mini, weig + dp_r(node, end))

            DP[start] = mini
            return DP[start]

    leng = dp_r(0, 9)
    print(DP)
    print(leng)


if __name__ == "__main__":
    diligencia_main()
