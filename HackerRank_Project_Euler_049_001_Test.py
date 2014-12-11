# Enter your code here. Read input from STDIN. Print output to STDOUT
Are_Primes = [True]*(10 ** 6 + 10 ** 5)
Primes = []
for i in xrange(2, int((10 ** 6 + 10 ** 5) ** 0.5)):
	if Are_Primes[i] == True:
		Primes.append(i)
		for j in xrange(i * i, int(10 ** 6 + 10 ** 5), i):
			Are_Primes[j] = False
for i in xrange(int((10 ** 6 + 10 ** 5) ** 0.5), int(10 ** 6 + 10 ** 5)):
	if Are_Primes[i] == True:
		Primes.append(i)
N, K = map(int, raw_input().split())
for i in range(len(Primes)):
	if Primes[i] < 1000:
		continue
	if Primes[i] > N:
		break
	for j in range(i + 1, len(Primes)):
		if 2 * N - Primes[j] + Primes[i] < 0:
			break
		Primes_K = 2 * Primes[j] - Primes[i]
		if Primes_K < 10 ** 6 + 10 ** 5 and Are_Primes[Primes_K] and sorted(str(Primes[i])) == sorted(str(Primes[j])) == sorted(str(Primes_K)):
			if K == 4:
				Primes_L = 2 * Primes_K - Primes[j]
				if Primes_L < 10 ** 6 + 10 ** 5 and Are_Primes[Primes_L] and sorted(str(Primes[i])) == sorted(str(Primes_L)):
					print  str(Primes[i]) + str(Primes[j]) + str(Primes_K) + str(Primes_L)
			else:
				print str(Primes[i]) + str(Primes[j]) + str(Primes_K)