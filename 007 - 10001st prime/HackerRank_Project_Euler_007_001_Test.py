# Enter your code here. Read input from STDIN. Print output to STDOUT
A = []
T = int(raw_input())
for i in range(T):
	Count = 0
	for j in range(104744):
		A.append(True)
	N = int(raw_input())
	for j in range(2, 104744):
		if A[j] == True:
			for k in range(j * j, 104744, j):
				A[k] = False
	for j in range(2, 104744):
		if A[j] == True:
			Count += 1
		if Count == N:
			print j
			break