Count = 0
for Digits in xrange(1, 9 // 2 + 1):
	Count += 20 * 30 ** (Digits - 1)
for Digits in xrange(3, 9, 4):
	Count += 100 * 500 ** (Digits // 4)
print Count
Wait = raw_input()