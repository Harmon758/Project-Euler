Triangle_File = open("p067_triangle.txt",'r')
Triangle = []
for Line in Triangle_File.readlines():
	Triangle.append(map(int, Line.split()))
for Row in range(99, 0, -1):
	for Column in range(Row):
		Triangle[Row - 1][Column] += max(Triangle[Row][Column], Triangle[Row][Column + 1])
print Triangle[0][0]
Wait = raw_input()