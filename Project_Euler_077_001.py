Number = 80
Are_Primes = [True]*Number
Primes = []
for i in xrange(2, int(Number ** 0.5)):
	if Are_Primes[i] == True:
		Primes.append(i)
		for j in xrange(i * i, Number, i):
			Are_Primes[j] = False
for i in xrange(int(Number ** 0.5), Number):
	if Are_Primes[i] == True:
		Primes.append(i)

End = 1
Count = [0]
while Count[End - 1] < 5000:
	Count = [1] + [0]*(End)
	for Prime in Primes:
		for i in range(Prime, End + 1):
			Count[i] += Count[i - Prime]
	End += 1
print End - 1
Wait = raw_input()