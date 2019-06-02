Matrix_File = open("p081_matrix.txt", 'r')
Matrix = [map(int, Row.split(',')) for Row in Matrix_File.readlines()]
Rows, Columns = len(Matrix), len(Matrix[0])
for Row in xrange(Rows - 2, -1, -1):
	Matrix[Row][Columns - 1] += Matrix[Row + 1][Columns - 1]
for Column in xrange(Columns - 2, -1, -1):
	Matrix[Rows - 1][Column] += Matrix[Rows - 1][Column + 1]
for Row in xrange(Rows - 2, -1, -1):
	for Column in xrange(Columns - 2, -1, -1):
		Matrix[Row][Column] += min(Matrix[Row + 1][Column], Matrix[Row][Column + 1])
print Matrix[0][0]
Wait = raw_input()