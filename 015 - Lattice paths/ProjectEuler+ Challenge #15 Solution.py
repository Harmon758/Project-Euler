from math import factorial

MODULO = True

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    routes = factorial(N + M) // (factorial(N) * factorial(M))
    print(routes % (10 ** 9 + 7) if MODULO else routes)
