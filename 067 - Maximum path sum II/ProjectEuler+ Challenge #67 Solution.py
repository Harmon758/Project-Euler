def maximum_top_to_bottom_total(triangle):
    for row in range(len(triangle) - 1, 0, -1):
        for column in range(row):
            triangle[row - 1][column] += max(
                triangle[row][column], triangle[row][column + 1]
            )
    return triangle[0][0]

try:
    with open("0067_triangle.txt",'r') as triangle_file:
        triangle = [list(map(int, line.split())) for line in triangle_file]
    print(maximum_top_to_bottom_total(triangle))
except FileNotFoundError:
    T = int(input())
    for testcase in range(T):
        N = int(input())
        triangle = [list(map(int, input().split())) for i in range(N)]
        print(maximum_top_to_bottom_total(triangle))
