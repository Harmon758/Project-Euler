# Enter your code here. Read input from STDIN. Print output to STDOUT
A = []
Primes = []
for i in xrange(0, int(10 ** 7)):
    A.append(True)
Primes.append(1)
for i in xrange(2, int(10 ** 3.5)):
    if A[i] == True:
        Primes.append(i)
        for j in xrange(i * i, int(10 ** 7), i):
            A[j] = False
for i in xrange(int(10 ** 3.5), int(10 ** 7)):
    if A[i] == True:
        Primes.append(i)
Pandigital_Primes = []
Numbers = "123456789"
for i in xrange(Primes.index(7652413), -1, -1):
    if not Numbers[:len(str(Primes[i]))].strip(str(Primes[i])):
        Pandigital_Primes.append(Primes[i])
T = int(raw_input())
for i in xrange(T):
    N = int(raw_input())
    if N >= 7652413:
        print 7652413
    else:
        j = 0
        while N < Pandigital_Primes[j] and j != len(Pandigital_Primes) - 1:
            j += 1
        if j != len(Pandigital_Primes) - 1:
            print Pandigital_Primes[j]
        else:
            print -1