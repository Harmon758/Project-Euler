# Enter your code here. Read input from STDIN. Print output to STDOUT
#Is_Pandigital
#Checks if a number is pandigital (1 - 9)
#Returns True if it is pandigital
#Returns False if it is not pandigital
def Is_Pandigital(Number):
	if len(str(Number)) > 9:
		return False
	Numbers = "123456789"
	return not Numbers[:len(str(Number))].strip(str(Number))

N, K = map(int, raw_input().split())
for i in xrange(2, N):
    Number = ""
    for j in range(1, K + 1):
        Number += str(i * j)
        if len(Number) == K:
            if Is_Pandigital(int(Number)):
                print i
                break
        elif len(Number) > K:
            break