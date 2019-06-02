def f(Number):
	return Number ** 2 - 3 * Number - 1

Are_Primes = [True]*(10 ** 7)
Primes = []
for i in xrange(2, int(10 ** 3.5)):
	if Are_Primes[i] == True:
		Primes.append(i)
		for j in xrange(i * i, 10 ** 7, i):
			Are_Primes[j] = False
for i in xrange(int(10 ** 3.5), 10 ** 7):
	if Are_Primes[i] == True:
		Primes.append(i)

def R(Number):
	for i in range(1, 10 ** 7):
		if f(i) % (Number ** 2) == 0:
			return i
	return 0

def SR(Number):
	Sum = 0
	for i in range(len(Primes)):
		if Primes[i] > Number:
			break
		Sum += R(Primes[i])
	return Sum

print SR(10 ** 7)
Wait = int(raw_input())