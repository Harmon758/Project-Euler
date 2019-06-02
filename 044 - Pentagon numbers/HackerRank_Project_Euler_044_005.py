# Enter your code here. Read input from STDIN. Print output to STDOUT
N, K = map(int, raw_input().split())
for n in range(K + 1, N):
    P_n = n * (3 * n - 1) / 2
    P_n_k = (n - K) * (3 * (n - K) - 1) / 2
    if (((24 * (P_n + P_n_k) + 1) ** 0.5 + 1) / 6).is_integer() or \
    ((24 * (P_n - P_n_k) + 1) > 0 and \
     (((24 * (P_n - P_n_k) + 1) ** 0.5 + 1) / 6).is_integer()):
        print P_n