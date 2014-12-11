T = int(raw_input())
for i in range(T):
    N, M = map(int, raw_input().split())
    k = min(N, M)
    paths = 1
    for j in range(k):
        paths = paths * (N + M - j) / (j + 1)
    print paths
Wait = raw_input()