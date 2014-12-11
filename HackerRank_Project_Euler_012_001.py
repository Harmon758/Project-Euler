# Enter your code here. Read input from STDIN. Print output to STDOUT
def Divisors(Number, Primes):
    Divisor_Count = 1
    Factor = Number
    for i in range(0, len(Primes)):
        if Primes[i] ** 2 > Factor:
            return Divisor_Count * 2
        Count = 1
        while Factor % Primes[i] == 0:
            Count += 1
            Factor = Factor / Primes[i]
        Divisor_Count *= Count
        if Factor == 1:
            return Divisor_Count
    return Divisor_Count

T = int(raw_input())
A = []
Primes = []
for j in xrange(0, 10 ** 4):
    A.append(True)
for j in xrange(2, 10 ** 2):
    if A[j] == True:
        Primes.append(j)
        for k in xrange(j * j, 10 ** 4, j):
            A[k] = False
for j in xrange(10 ** 2, 10 ** 4):
    if A[j] == True:
        Primes.append(j)
for i in range(0, T):
    N = int(raw_input())
    Count = 2
    Divisor_Count = 0
    Odd = 1
    Even = 1
    while Divisor_Count <= N:
        if Count % 2 == 0:
            Even = Divisors(Count + 1, Primes)
            Divisor_Count = Even * Odd
        else:
            Odd = Divisors((Count + 1) / 2, Primes)
            Divisor_Count = Even * Odd
        Count += 1
    print Count * (Count - 1) / 2