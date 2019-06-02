# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for i in range(T):
	A, B, C, Sum = 1, 2, 3, 2
	N = int(raw_input())
	if N < 2:
		print 0
	else:
		while C < N:
			if C % 2 == 0:
				Sum += C
			A, B, C = B, C, B + C
		print Sum