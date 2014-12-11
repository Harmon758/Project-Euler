Number = int(19293949596979899 ** 0.5) + 1
while True:
	Str_Number = str(Number ** 2)
	for i in range(9):
		if int(Str_Number[i * 2]) != i + 1:
			break
	else:
		break
	Number -= 2
Number *= 10
print Number
print Number ** 2
Wait = raw_input()