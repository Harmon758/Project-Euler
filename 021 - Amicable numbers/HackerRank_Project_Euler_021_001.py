# Enter your code here. Read input from STDIN. Print output to STDOUT
def Sum_Of_Divisors(Number, Primes):
    Sum = 1
    Factor = Number
    i = 0
    while i < len(Primes) and Primes[i] ** 2 <= Factor and Factor > 1:
        if Factor % Primes[i] == 0:
            Temp = Primes[i] ** 2
            Factor = Factor / Primes[i]
            while Factor % Primes[i] == 0:
                Temp *= Primes[i]
                Factor = Factor / Primes[i]
            Sum *= (Temp - 1) / (Primes[i] - 1)
        i += 1
    if Factor > 1:
        Sum *= Factor + 1
    return Sum - Number

A = []
Primes = []
for j in xrange(0, int(10 ** 2.5)):
    A.append(True)
for j in xrange(2, int(10 ** 1.25)):
    if A[j] == True:
        Primes.append(j)
        for k in xrange(j * j, int(10 ** 2.5), j):
            A[k] = False
for j in xrange(int(10 ** 1.25), int(10 ** 2.5)):
    if A[j] == True:
        Primes.append(j)
T = int(raw_input())
Largest = 0
Amicable = []
for i in range(T):
    N = int(raw_input())
    Sum = 0
    if Largest < N:
        for j in range(2, N):
            Divisors1 = Sum_Of_Divisors(j, Primes)
            if Divisors1 > j:
                Divisors2 = Sum_Of_Divisors(Divisors1, Primes)
                if Divisors2 == j:
                    if Divisors1 < N:
                        Sum += j + Divisors1
                    else:
                        Sum += j
                    if j > Largest:
                        Amicable.append(j)
                        Amicable.append(Divisors1)
        Largest = N
    else:
        for j in range(len(Amicable)):
            if Amicable[j] < N:
                Sum += Amicable[j]
    print Sum