Are_Primes = [True]*(10 ** 5)
Primes = []
for i in xrange(2, int(10 ** 2.5)):
	if Are_Primes[i] == True:
		Primes.append(i)
		for j in xrange(i * i, int(10 ** 5), i):
			Are_Primes[j] = False
for i in xrange(int(10 ** 2.5), int(10 ** 5)):
	if Are_Primes[i] == True:
		Primes.append(i)
for i in range(len(Primes)):
	if Primes[i] < 1000:
		continue
	for j in range(i + 1, len(Primes)):
		Primes_K = 2 * Primes[j] - Primes[i]
		if Primes_K < 10000 and Are_Primes[Primes_K] and sorted(str(Primes[i])) == sorted(str(Primes[j])) == sorted(str(Primes_K)):
			print str(Primes[i]) + str(Primes[j]) + str(Primes_K)
Wait = raw_input()