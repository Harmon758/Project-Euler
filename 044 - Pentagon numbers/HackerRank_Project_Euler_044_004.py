# Enter your code here. Read input from STDIN. Print output to STDOUT
def Pentagonal(Number):
    if 24 * Number + 1 > 0:
        return (((24 * Number + 1) ** 0.5 + 1) / 6).is_integer()
    else:
        return False
    
N, K = map(int, raw_input().split())
for n in range(K + 1, N):
    P_n = n * (3 * n - 1) / 2
    P_n_k = (n - K) * (3 * (n - K) - 1) / 2
    if Pentagonal(P_n + P_n_k) or Pentagonal(P_n - P_n_k):
        print P_n