# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for i in range(T):
	N = int(raw_input())
	Largest = 0
	for j in range(1, N / 3 + 1):
		k = (2 * j * N - N * N) / (2 * j - 2 * N)
		l = N - k - j
		if l * l == k * k +  j * j and l * k * j > Largest:
			Largest = l * k * j
	if Largest == 0:
		print "-1"
	else:
		print Largest