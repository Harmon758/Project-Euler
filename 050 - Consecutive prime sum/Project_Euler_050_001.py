Are_Primes = [True]*(10 ** 6)
Primes = []
Primes_Sum = [0]
Count = 1
for i in xrange(2, 10 ** 3):
	if Are_Primes[i] == True:
		Primes.append(i)
		Primes_Sum.append(Primes_Sum[Count - 1] + i)
		Count += 1
		for j in xrange(i * i, 10 ** 6, i):
			Are_Primes[j] = False
for i in xrange(10 ** 3, 10 ** 6):
	if Are_Primes[i] == True:
		Primes.append(i)
		Primes_Sum.append(Primes_Sum[Count - 1] + i)
		Count += 1
Largest = 0
Count = 0
for i in xrange(len(Primes_Sum) - 1):
	if Primes[i] >= 10 ** 6:
		break
	for j in xrange(i - (Count + 1), -1, -1):
		if Primes_Sum[i] - Primes_Sum[j] >= 10 ** 6:
			break
		if Are_Primes[Primes_Sum[i] - Primes_Sum[j]] and i - j > Count:
			Largest = Primes_Sum[i] - Primes_Sum[j]
			Count = i - j
print Largest, Count
Wait = raw_input()