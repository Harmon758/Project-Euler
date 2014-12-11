# Enter your code here. Read input from STDIN. Print output to STDOUT
Grid = []
Largest = 0
for i in range(0, 20):
    Grid.append(map(int, raw_input().split()))
for i in range(0, 20):
    for j in range(0, 20):
        if i <= 16 and Grid[i][j] * Grid[i + 1][j] * Grid[i + 2][j] * Grid[i + 3][j] > Largest:
            Largest = Grid[i][j] * Grid[i + 1][j] * Grid[i + 2][j] * Grid[i + 3][j]
        if j <= 16 and Grid[i][j] * Grid[i][j + 1] * Grid[i][j + 2] * Grid[i][j + 3] > Largest:
            Largest = Grid[i][j] * Grid[i][j + 1] * Grid[i][j + 2] * Grid[i][j + 3]
        if i <= 16 and j <= 16 and Grid[i][j] * Grid[i + 1][j + 1] * Grid[i + 2][j + 2] * Grid[i + 3][j + 3] > Largest:
            Largest = Grid[i][j] * Grid[i + 1][j + 1] * Grid[i + 2][j + 2] * Grid[i + 3][j + 3]
        if i >= 3 and j <= 16 and Grid[i][j] * Grid[i - 1][j + 1] * Grid[i - 2][j + 2] * Grid[i - 3][j + 3] > Largest:
            Largest = Grid[i][j] * Grid[i - 1][j + 1] * Grid[i - 2][j + 2] * Grid[i - 3][j + 3]
print Largest