# Enter your code here. Read input from STDIN. Print output to STDOUT
N = 1000
Max = 0
Max_p = 0
if N % 2 == 1:
	N += 1
for p in range(N, N / 8 - 1, -2):
	Count = 0
	for a in range(2, int(p / (2 + 2 ** 0.5)) + 1):
		if p * (p - 2 * a) % (2 * (p - a)) == 0:
			Count += 1
	if Count >= Max:
		Max = Count
		Max_p = p
print Max_p
Wait = raw_input()