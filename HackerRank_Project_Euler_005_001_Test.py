# Enter your code here. Read input from STDIN. Print output to STDOUT
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

T = int(raw_input())
for i in range(T):
	Product = 1
	N = int(raw_input())
	for j in range(2, N + 1):
		Product = Product * j / gcd(Product, j)
	print Product