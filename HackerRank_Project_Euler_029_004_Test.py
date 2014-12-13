# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import log
from math import floor

def lcm(k, i):
    if i % k == 0:
        return i
    else:
        i_ = i
        k_ = k
        r = i % k;
        while (r != 0):
            i = k
            k = r
            r = i % k
        return i_ * k_ / k

N = int(raw_input())
maxPow = int(floor(log(N) / log(2)))
dupesPerPow = [0]*(maxPow + 1)
numOfPow = [0]*(maxPow + 1)
totDupes = 0
		
for i in range(2, maxPow + 1):
    powOverlap = [False]*(N + 1)
    for k in range(1, i):
        spacing = lcm(k, i) / i
        for n in range(0, k * N / i + 1, spacing):
            powOverlap[n] = True
    count = 0
    for j in range(2, N + 1):
        if powOverlap[j]:
            count += 1
    dupesPerPow[i] = count

sqrtN = int(N ** 0.5)
powersNotToRepeat = [False]*(sqrtN + 1)
for i in range(2, sqrtN + 1):
    if not powersNotToRepeat[i]:
        p = 2
        while (i ** p <= N):
            numOfPow[p] += 1
            if i ** p <= sqrtN:
                powersNotToRepeat[int(i ** p)] = True
            p += 1

for p in range(2, maxPow + 1):
    totDupes += numOfPow[p] * dupesPerPow[p];
print (N - 1) * (N - 1) - totDupes