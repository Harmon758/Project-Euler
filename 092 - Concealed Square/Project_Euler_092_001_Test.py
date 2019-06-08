def Square_Digit_Sum(Number):
	Number_String = str(Number)
	Sum = 0
	for Digit in Number_String:
		Sum += int(Digit) ** 2
	return Sum

is89 = [ -1 for i in xrange(10 ** 7) ]
Count = 0
for i in xrange(10 ** 7):
	Number = i
	while Number != 89 and Number != 1:
		if is89[Number] == 1:
			Number = 89
		elif is89[Number] == 0:
			Number = 1
		else:
			Number = Square_Digit_Sum(Number)
	if Number == 89:
		is89[i] = 1
		Count += 1
	elif Number == 1:
		is89[i] = 0
print Count
Wait = raw_input()