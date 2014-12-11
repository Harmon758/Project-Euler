# Enter your code here. Read input from STDIN. Print output to STDOUT

#Is_Pandigital
#Checks if a number is pandigital (1 - 9)
#Returns True if it is pandigital
#Returns False if it is not pandigital
def Is_Pandigital(Number):
	Numbers = "123456789"
	return not Numbers[:len(str(Number))].strip(str(Number))

Largest = 0
for i in xrange(10000, 1, -1):
	Number = ""
	for j in range(1, 10):
		Number += str(i * j)
		if len(Number) == 9:
			if Is_Pandigital(int(Number)):
				if Number > Largest:
					Largest = Number
				break
		elif len(Number) > 9:
			break
print Largest
Wait = raw_input()