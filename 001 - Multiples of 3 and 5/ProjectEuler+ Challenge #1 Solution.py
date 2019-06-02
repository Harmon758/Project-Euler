# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for i in range(T):
	Sum = 0
	N = int(raw_input())
	Temp = (N - 1) // 3
	Sum += (Temp * (3 + Temp * 3)) // 2
	Temp = (N - 1) // 5
	Sum += (Temp * (5 + Temp * 5)) // 2
	Temp = (N - 1) // 15
	Sum -= (Temp * (15 + Temp * 15)) // 2
	print Sum