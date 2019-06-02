from math import log10

Count = 0
for i in range(1, 10):
	Count += int(1 / (1 - log10(i)))
print Count
Wait = raw_input()