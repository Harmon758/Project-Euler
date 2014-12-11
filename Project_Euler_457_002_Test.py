Are_Primes = [True]*(10 ** 7)
Primes_Squared = []
for i in xrange(2, int(10 ** 3.5)):
	if Are_Primes[i] == True:
		Primes_Squared.append(i)
		for j in xrange(i * i, 10 ** 7, i):
			Are_Primes[j] = False
for i in xrange(int(10 ** 3.5), 10 ** 7):
	if Are_Primes[i] == True:
		Primes_Squared.append(i)

def SR(Number):
	Sum = 0
	for i in range(len(Primes_Squared)):
		if Primes_Squared[i] > Number:
			break
		for j in range(1, 10 ** 7):
			if j ** 2 - 3 * j - 1 % Primes_Squared[i] == 0:
				Sum += i
	return Sum

print SR(10 ** 7)
Wait = int(raw_input())