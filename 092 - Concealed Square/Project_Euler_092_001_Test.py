def Square_Digit_Sum(Number):
	Number_String = str(Number)
	Sum = 0
	for Digit in Number_String:
		Sum += int(Digit) ** 2
	return Sum

Count = 0
for i in range(10 ** 7):
	Number = i
	while Number != 89 and Number != 1:
		Number = Square_Digit_Sum(Number)
	if Number == 89:
		Count += 1
print Count
Wait = raw_input()