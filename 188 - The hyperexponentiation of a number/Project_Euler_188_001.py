#a, b = map(int, raw_input().split)
a = 1777
b = 1855
Number = 1
for i in range(b):
	Number = pow(a, Number, 10 ** 8)
print Number
Wait = raw_input()