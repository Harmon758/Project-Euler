triangle = []
with open("0067_triangle.txt",'r') as triangle_file:
    for line in triangle_file:
        triangle.append(list(map(int, line.split())))

for row in range(len(triangle) - 1, 0, -1):
    for column in range(row):
        triangle[row - 1][column] += max(
            triangle[row][column], triangle[row][column + 1]
        )
print(triangle[0][0])
