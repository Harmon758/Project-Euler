"""
def f(k, n):
	Sum = 0
	for i in range(1, n + 1):
		Sum += i ** k
	return Sum

def S(k, n):
	Sum = 0
	for i in range(1, n + 1):
		Sum += f(k, i)
	return Sum

def T(k, n, p):
	return S(k, n) % p
"""

def T(k, n, p):
	Sum = 0
	for i in xrange(1, n + 1):
		for j in xrange(1, i + 1):
			Sum += pow(j, k, p)
	return Sum % p

print T(10000, 10 ** 12, 2 * 10 ** 9)
Wait = raw_input()