from bisect import bisect_left
from math import ceil, log, sqrt

N_UPPER_BOUND = 10 ** 18

primorial_limit = max(6, ceil(log(N_UPPER_BOUND, 4)))
sieve_limit = ceil(
    primorial_limit * (log(primorial_limit) + log(log(primorial_limit)))
)

sieve = [True] * sieve_limit
primes = []
primorials = [1]
for number in range(2, int(sqrt(sieve_limit))):
    if sieve[number]:
        primes.append(number)
        primorials.append(number * primorials[-1])
        for multiple in range(number * number, sieve_limit, number):
            sieve[multiple] = False
for number in range(int(sqrt(sieve_limit)), sieve_limit):
    if sieve[number]:
        primes.append(number)
        primorials.append(number * primorials[-1])

T = int(input())
for test_case in range(T):
    N = int(input())
    index = bisect_left(primorials, N) -1
    print(primorials[index])
