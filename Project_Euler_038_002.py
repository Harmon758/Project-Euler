# Enter your code here. Read input from STDIN. Print output to STDOUT

#Is_Pandigital
#Checks if a number is pandigital (1 - 9)
#Returns True if it is pandigital
#Returns False if it is not pandigital
def Is_Pandigital(Number):
	Numbers = "123456789"
	return not Numbers[:len(str(Number))].strip(str(Number))

Largest = 0
Flag = False
for i in xrange(10000, 8999, -1):
	Number = ""
	for j in range(1, 10):
		Number += str(i * j)
		if len(Number) == 9:
			if Is_Pandigital(int(Number)):
				print Number
				Flag = True
				break
		elif len(Number) > 9:
			break
	if Flag:
		break
Wait = raw_input()