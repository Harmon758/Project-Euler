# Enter your code here. Read input from STDIN. Print output to STDOUT
N, K = map(int, raw_input().split())
for n in range(K + 1, N):
    if (((24 * (n * (3 * n - 1) / 2 + (n - K) * (3 * (n - K) - 1) / 2) + 1) ** 0.5 + 1) / 6).is_integer() or \
    ((24 * (n * (3 * n - 1) / 2 - (n - K) * (3 * (n - K) - 1) / 2) + 1) > 0 and (((24 * (n * (3 * n - 1) / 2 - (n - K) * (3 * (n - K) - 1) / 2) + 1) ** 0.5 + 1) / 6).is_integer()):
        print n * (3 * n - 1) / 2