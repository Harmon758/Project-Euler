def Reverse(Number):
	Reverse = 0
	while Number != 0:
		Temp = Number % 10
		Reverse = Reverse * 10 + Temp
		Number /= 10
	return Reverse

Count = 0
for i in range(10, 10000):
	Number = i
	Reverse_Number = 0
	Count2 = 0
	while Reverse_Number != Number:
		Reverse_Number = Reverse(Number)
		Number += Reverse_Number
		Reverse_Number = Reverse(Number)
		Count2 += 1
		if Count2 == 50:
			break
	if Count2 == 50:
		Count += 1
		continue
print Count
Wait = raw_input()