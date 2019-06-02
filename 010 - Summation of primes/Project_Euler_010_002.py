A = [True]*int(3 * 10 ** 6)
B = []
Sums = []
Sums.append(0)
for j in xrange(2, int((3 * 10 ** 6) ** 0.5)):
    if A[j] == True:
        B.append(j)
        Sums.append(Sums[len(Sums) - 1] + j)
        for k in xrange(j * j, int(3 * 10 ** 6), j):
            A[k] = False
for j in xrange(int((3 * 10 ** 6) ** 0.5), int(3 * 10 ** 6)):
    if A[j] == True:
        B.append(j)
        Sums.append(Sums[len(Sums) - 1] + j)
N = 2000000
Count = len(B) / 2
Interval = len(B) / 4
while B[Count] <= N or B[Count - 1] > N:
	if B[Count] > N:
		Count -= Interval
	else:
		Count += Interval
	if Interval != 1:
		Interval /= 2
print Sums[Count]
Wait = raw_input()