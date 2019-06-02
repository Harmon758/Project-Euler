# Enter your code here. Read input from STDIN. Print output to STDOUT
from random import randrange

def Miller_Rabin(n, k):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d /= 2
        s += 1
    for i in range(k):
        a = randrange(2, n)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(s - 1):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            return False
    return True

k = 5
N = int(raw_input())
N = float(N) / 100
Average = 1
Spacing = 2
Offset = 1
Count = 0
Total = 1
while Average >= N:
    if Miller_Rabin(Offset + Spacing, k):
        Count += 1
    if Miller_Rabin(Offset + 2 * Spacing, k):
        Count += 1
    if Miller_Rabin(Offset + 3 * Spacing, k):
        Count += 1
    Offset += Spacing * 4
    Spacing += 2
    Total += 4
    Average = float(Count) / Total
print Spacing - 1