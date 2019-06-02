def ChecK(Number1, Number2, Check):
	Str_Number1 = str(Number1)
	Str_Number2 = str(Number2)
	if len(Str_Number1) != len(Str_Number2):
		return False
	Count = 0
	for i in len(Str_Number1):
		if Str_Number1[i] == Str_Number2[i]:
			Count += 1
			if Count > Check:
				return False
	if Count == Check:
		return True
	return False

Guesses = []
Guesses_Count = 0
Number = 0
while True:
	Guesses.append(raw_input().split())
	Guesses[Guesses_Count][0] = int(Guesses[Guesses_Count][0])
	Guesses[Guesses_Count][1] = Guesses[Guesses_Count][1][1]
	Guesses_Count += 1
	Multiple_Flag = False
	Found_Flag = False
	for i in xrange(10 ** 15, 10 ** 16):
		for j in range(len(Guesses)):
			if not Check(i, Guesses[j][0], Guesses[j][1]):
				break
		else:
			if Found_Flag == True:
				Multiple_Flag = True
				break
			Number = i
			Found_Flag = True
	if Multiple_Flag == True:
		continue
	if Found_Flag == True:
		print Number
		break
Wait = raw_input()