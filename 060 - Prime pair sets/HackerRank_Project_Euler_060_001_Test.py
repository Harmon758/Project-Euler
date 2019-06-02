Number = 10 ** 6
Are_Primes = [True]*Number
Primes = []
for i in xrange(2, int(Number ** 0.5)):
	if Are_Primes[i] == True:
		Primes.append(i)
		for j in xrange(i * i, int(Number), i):
			Are_Primes[j] = False
for i in xrange(int(Number ** 0.5), int(Number)):
	if Are_Primes[i] == True:
		Primes.append(i)

N, K = map(int, raw_input().split())
Indexes = []
Sums = []
Flag = False
for i in range(K):
	Indexes.append(i)
while Primes[Indexes[0]] < N:
	Flag = False
	for i in range(K - 1):
		for j in range(i + 1, K):
			if not (Are_Primes[int(str(Primes[Indexes[i]]) + str(Primes[Indexes[j]]))] and Are_Primes[int(str(Primes[Indexes[j]]) + str(Primes[Indexes[i]]))]):
				Flag = True
				break
		if Flag:
			break
	else:
		Sum = 0
		for i in range(K):
			Sum += Primes[Indexes[i]]
		Sums.append(Sum)
	for i in range(K - 1, -1, -1):
		if Primes[Indexes[i] + 1] < N:
			Indexes[i] += 1
			for j in range(i + 1, K):
				Indexes[j] = Indexes[j - 1] + 1
			break
	else:
		break
Sums.sort()
for i in range(len(Sums)):
	print Sums[i]