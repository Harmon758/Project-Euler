# Enter your code here. Read input from STDIN. Print output to STDOUT
N = 10000
Flag = True
j = 0
while Flag:
	j += 1
	P_j = j * (3 * j - 1) / 2
	for k in range(j - 1, 0, -1):
		P_k = k * (3 * k - 1) / 2
		if (((24 * (P_j + P_k) + 1) ** 0.5 + 1) / 6).is_integer() and \
		((24 * (P_j - P_k) + 1) > 0 and \
		 (((24 * (P_j - P_k) + 1) ** 0.5 + 1) / 6).is_integer()):
			print P_j - P_k
			Flag = False
Wait = raw_input()