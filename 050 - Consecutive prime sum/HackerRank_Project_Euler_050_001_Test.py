# Enter your code here. Read input from STDIN. Print output to STDOUT
Are_Primes = [True]*(10 ** 4)
Primes = []
Primes_Sum = [0]
Count = 1
for i in xrange(2, 10 ** 2):
	if Are_Primes[i] == True:
		Primes.append(i)
		Primes_Sum.append(Primes_Sum[Count - 1] + i)
		Count += 1
		for j in xrange(i * i, 10 ** 4, i):
			Are_Primes[j] = False
for i in xrange(10 ** 2, 10 ** 4):
	if Are_Primes[i] == True:
		Primes.append(i)
		Primes_Sum.append(Primes_Sum[Count - 1] + i)
		Count += 1
T = int(raw_input())
for i in range(T):
	N = int(raw_input())
	Largest = 0
	Count = 0
	for j in range(len(Primes_Sum)):
		if Primes[j] >= N:
			break
		for k in range(j - 1, -1, -1):
			if Primes_Sum[j] - Primes_Sum[k] >= N:
				break
			if Are_Primes[Primes_Sum[j] - Primes_Sum[k]] and j - k > Count:
				Largest = Primes_Sum[j] - Primes_Sum[k]
				Count = j - k
	print Largest, Count