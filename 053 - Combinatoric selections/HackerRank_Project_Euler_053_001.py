# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import factorial

N, K = map(int, raw_input().split())
Count = 0
for n in range(1, N + 1):
    for r in range(1, n):
        if factorial(n) / (factorial(r) * factorial(n - r)) > K:
            Count += n - 2 * r + 1
            break
print Count