# Enter your code here. Read input from STDIN. Print output to STDOUT
A = [True]*(5 * 10 ** 5)
Primes = []
for i in xrange(2, int((5 * 10 ** 5) ** 0.5)):
    if A[i] == True:
        Primes.append(i)
        for j in xrange(i * i, 5 * 10 ** 5, i):
            A[j] = False
for i in xrange(int((5 * 10 ** 5) ** 0.5), 5 * 10 ** 5):
    if A[i] == True:
        Primes.append(i)
T = int(raw_input())
for i in range(T):
    N = int(raw_input())
    j = 0
    Count = 0
    while Primes[j] <= N:
        if ((float(N - Primes[j]) / 2) ** 0.5).is_integer():
            Count += 1
        j += 1
    print Count