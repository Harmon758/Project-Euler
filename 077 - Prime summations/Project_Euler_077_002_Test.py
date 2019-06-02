Number = 100
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

Count, End = [1], 0
while Count[End] < 5000:
	Count.append(0)
	End += 1
	for Prime in Primes:
		if Prime <= End:
			Count[End] += Count[End - Prime]
		else:
			break
print End
Wait = raw_input()