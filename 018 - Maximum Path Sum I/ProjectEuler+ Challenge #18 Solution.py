T = int(input())
for testcase in range(T):
    triangle = []
    N = int(input())
    for i in range(N):
        triangle.append(list(map(int, input().split())))

    for row in range(N - 1, 0, -1):
        for column in range(row):
            triangle[row - 1][column] += max(
                triangle[row][column], triangle[row][column + 1]
            )
    print(triangle[0][0])
