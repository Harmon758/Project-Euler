# Enter your code here. Read input from STDIN. Print output to STDOUT
def Sum_Of_Divisors(Number, Primes):
    Sum = 1
    Factor = Number
    i = 0
    while i < len(Primes) and Primes[i] ** 2 <= Factor and Factor > 1:
        if Factor % Primes[i] == 0:
            Temp = Primes[i] ** 2
            Factor = Factor // Primes[i]  # Integer division in Python 3
            while Factor % Primes[i] == 0:
                Temp *= Primes[i]
                Factor = Factor // Primes[i]  # Integer division in Python 3
            Sum *= (Temp - 1) // (Primes[i] - 1)  # Integer division in Python 3
        i += 1
    if Factor > 1:
        Sum *= Factor + 1
    return Sum - Number

A = []
Primes = []
for j in range(0, int(10 ** 2.5)):  # Range function in Python 3 doesn't include the stop value
    A.append(True)
for j in range(2, int(10 ** 1.25)):  # Range function in Python 3 doesn't include the stop value
    if A[j] == True:
        Primes.append(j)
        for k in range(j * j, int(10 ** 2.5), j):  # Range function in Python 3 doesn't include the stop value
            A[k] = False
for j in range(int(10 ** 1.25), int(10 ** 2.5)):  # Range function in Python 3 doesn't include the stop value
    if A[j] == True:
        Primes.append(j)
T = int(input())  # Use input() instead of raw_input() in Python 3
Largest = 0
Amicable = []
for i in range(T):
    N = int(input())  # Use input() instead of raw_input() in Python 3
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
    print(Sum)  # Add an argument to print the result
