def Sum_Of_Divisors(Number, Primes):
    Sum = 1
    Factor = Number
    i = 0
    while i < len(Primes) and Primes[i] ** 2 <= Factor and Factor > 1:
        if Factor % Primes[i] == 0:
            Temp = Primes[i] ** 2
            Factor = Factor / Primes[i]
            while Factor % Primes[i] == 0:
                Temp *= Primes[i]
                Factor = Factor / Primes[i]
            Sum *= (Temp - 1) / (Primes[i] - 1)
        i += 1
    if Factor > 1:
        Sum *= Factor + 1
    return Sum - Number

A = [True]*int(10 ** 2.5)
Primes = []
for j in xrange(2, int(10 ** 1.25)):
    if A[j] == True:
        Primes.append(j)
        for k in xrange(j * j, int(10 ** 2.5), j):
            A[k] = False
for j in xrange(int(10 ** 1.25), int(10 ** 2.5)):
    if A[j] == True:
        Primes.append(j)

Abundant = []
for i in xrange(12, 28124):
    if Sum_Of_Divisors(i, Primes) > i:
        Abundant.append(i)
"""
Sums = []
for i in xrange(len(Abundant)):
    for j in xrange(i, len(Abundant)):
        if Abundant[i] + Abundant[j] <= 28124:
            Sums.append(Abundant[i] + Abundant[j])
        else:
            break
"""
Sum = 0
for i in range(28124):
	Flag = False
	for j in xrange(len(Abundant)):
		for k in xrange(j, len(Abundant)):
			if Abundant[j] + Abundant[k] == i:
				Flag = True
				break
			elif Abundant[j] + Abundant[k] > i:
				break
		if Flag == True:
			break
	if Flag == False:
		Sum += i
print Sum
Wait = raw_input()