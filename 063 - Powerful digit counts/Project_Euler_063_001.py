Count = 0
for i in range(1, 100):
	for j in range(1, 10):
		if j ** i >= 10 ** (i - 1) and j ** i < 10 ** i:
			Count += 1
			print j, i, j ** i
		elif j ** i >= 10 ** i:
			break
print Count
Wait = raw_input()