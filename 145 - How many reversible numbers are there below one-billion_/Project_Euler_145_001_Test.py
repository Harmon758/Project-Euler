#Reverse
#Reverses a number's digits
#12345 -> 54321
def Reverse(Number):
	Reverse = 0
	while Number != 0:
		Temp = Number % 10
		Reverse = Reverse * 10 + Temp
		Number /= 10
	return Reverse

def Sum_Reverse(Number):
	return Number + Reverse(Number)

Count = 0
for Number in xrange(1, 10 ** 9):
	Sum_Reversed_Number = Sum_Reverse(Number)
	while Sum_Reversed_Number > 0:
		if Sum_Reversed_Number % 2 == 0:
			break
	else:
		Count += 1
print Count
Wait = raw_input()