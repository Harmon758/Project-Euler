# Enter your code here. Read input from STDIN. Print output to STDOUT
#http://blog.dreamshire.com/project-euler-43-solution/
from math import factorial

def permutation(number, string):
    if len(string) == 1:
		return string
    qoutient, remainder = divmod(number, factorial(len(string) - 1))
    return string[qoutient] + permutation(remainder, string[:qoutient] + string[qoutient + 1:])

N = int(raw_input())
Numbers = "0123456789"
Sum = 0
if N == 9:
	for j in range(24):
		Number = permutation(j, "0134") + "952867"
		if int(Number[2:5]) % 3 == 0 and int(Number[1:4]) % 2 == 0:
			Sum += int(Number)
		Number = permutation(j, "0146") + "357289"
		if int(Number[2:5]) % 3 == 0 and int(Number[1:4]) % 2 == 0:
			Sum += int(Number)
else:
	for i in xrange(factorial(N + 1)):
		Number = permutation(i, Numbers[:N + 1])
		if len(Number) >= 9 and int(Number[6:9]) % 13 != 0:
			continue
		if len(Number) >= 8 and int(Number[5:8]) % 11 != 0:
			continue
		if len(Number) >= 7 and int(Number[4:7]) % 7 != 0:
			continue
		if len(Number) >= 6 and int(Number[3:6]) % 5 != 0:
			continue
		if len(Number) >= 5 and int(Number[2:5]) % 3 != 0:
			continue
		if int(Number[1:4]) % 2 != 0:
			continue
		Sum += int(Number)
print Sum