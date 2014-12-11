# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for i in range(T):
    N, M = map(int, raw_input().split())
    k = min(N, M)
    paths = 1
    for j in range(k):
        paths = paths * (N + M - j) / (j + 1)
    print paths % (10 ** 9 + 7)