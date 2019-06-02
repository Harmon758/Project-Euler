# Enter your code here. Read input from STDIN. Print output to STDOUT
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

T = int(raw_input())
for i in range(T):
    N = int(raw_input())
    Primes_N = []
    Longest = 0
    Longest_Number = 0
    for Prime in Primes:
        if Prime >= N:
            break;
        else:
            Primes_N.append(Prime)
    for j in Primes_N[::-1]:
        Count = 1
        if pow(10, Count, j) == 0:
            continue
        while pow(10, Count, j) - 1 != 0:
            Count += 1
        if j - Count == 1:
            if Count >= Longest:
                Longest_Number = j
            break
        if Count >= Longest:
            Longest = Count
            Longest_Number = j
    print Longest_Number