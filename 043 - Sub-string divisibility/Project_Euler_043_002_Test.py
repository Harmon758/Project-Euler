from math import factorial

def permutation(number, string):
    if len(string) == 1:
		return string
    qoutient, remainder = divmod(number, factorial(len(string) - 1))
    return string[qoutient] + permutation(remainder, string[:qoutient] + string[qoutient + 1:])

Sum = 0
for j in range(24):
	Number = permutation(j, "0134") + "952867"
	if int(Number[2:5]) % 3 == 0 and int(Number[1:4]) % 2 == 0:
		Sum += int(Number)
	Number = permutation(j, "0146") + "357289"
	if int(Number[2:5]) % 3 == 0 and int(Number[1:4]) % 2 == 0:
		Sum += int(Number)
print Sum
Wait = raw_input()