# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
A = [True]*(10 ** 6)
B = []
Sums = []
Sums.append(0)
for j in xrange(2, 10 ** 3):
    if A[j] == True:
        B.append(j)
        Sums.append(Sums[len(Sums) - 1] + j)
        for k in xrange(j * j, 10 ** 6, j):
            A[k] = False
for j in xrange(10 ** 3, 10 ** 6):
    if A[j] == True:
        B.append(j)
        Sums.append(Sums[len(Sums) - 1] + j)
B.append(10 ** 6 + 1)
for i in range(0, T):
    N = int(raw_input())
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