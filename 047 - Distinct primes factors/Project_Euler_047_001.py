# Enter your code here. Read input from STDIN. Print output to STDOUT
Flag = True
Consecutive = 0
Number = 0
while Flag:
	Number += 1
	Factors = set()
	Factor = Number
	while Factor != 1:
		for i in xrange(2, int(Factor ** 0.5 + 1)):
			if Factor % i == 0:
				Factors.add(i)
				Factor /= i
				break
		else:
			Factors.add(Factor)
			break
	if len(Factors) == 4:
		Consecutive += 1
		if Consecutive == 4:
			print Number - 3
			Flag = False
	else:
		Consecutive = 0
Wait = raw_input()