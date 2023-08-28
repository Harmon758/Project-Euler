from math import prod

grid = [[0] * 23] * 3
for _ in range(20):
    grid.append(list(map(int, input().split())) + [0] * 3)
grid.extend([[0] * 23] * 3)
print(max(
    prod(
        grid[row + direction[0] * offset][column + direction[1] * offset]
        for offset in range(4)
    )
    for direction in ((0, 1), (1, 0), (1, 1), (-1, 1))
    for row in range(3, 23) for column in range(20)
))
