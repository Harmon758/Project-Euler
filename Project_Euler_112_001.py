def Bouncy(Number):
	Str_Number = str(Number)
	Greater_Flag = False
	Lesser_Flag = False
	for i in range(1, len(Str_Number)):
		if Str_Number[i] > Str_Number[i - 1]:
			Greater_Flag = True
		elif Str_Number[i] < Str_Number[i - 1]:
			Lesser_Flag = True
		if Greater_Flag == True and Lesser_Flag == True:
			return True
	return False
Number = 99
Count = 0
while True:
	Number += 1
	if Bouncy(Number):
		Count += 1
	if float(Count) / Number == 0.99:
		print Number
		break
Wait = raw_input()