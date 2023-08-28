from math import sqrt

LIMIT = 10_000

sieve = [True] * LIMIT
primes = []
for number in range(2, int(sqrt(LIMIT))):
    if sieve[number]:
        primes.append(number)
        for multiple in range(number * number, LIMIT, number):
            sieve[multiple] = False
for number in range(int(sqrt(LIMIT)), LIMIT):
    if sieve[number]:
        primes.append(number)

def divisors(number):
    divisor_count = 1
    factor = number
    for prime in primes:
        if prime ** 2 > factor:
            return divisor_count * 2
        count = 1
        while factor % prime == 0:
            count += 1
            factor //= prime
        divisor_count *= count
        if factor == 1:
            return divisor_count
    return divisor_count

T = int(input())
for testcase in range(T):
    N = int(input())
    count = 2
    divisor_count = 0
    odd = 1
    even = 1
    while divisor_count <= N:
        if count % 2:
            odd = divisors((count + 1) // 2)
            divisor_count = even * odd
        else:
            even = divisors(count + 1)
            divisor_count = even * odd
        count += 1
    print(count * (count - 1) // 2)
