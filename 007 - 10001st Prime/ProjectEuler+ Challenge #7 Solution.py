from math import ceil, log

N_upper_bound = 10 ** 4 + 1  # 10001 (+ 1) for Project Euler Problem
limit = ceil(N_upper_bound * (log(N_upper_bound) + log(log(N_upper_bound))))

limit += 1
numbers = [True] * limit
primes = []

T = int(input())
for _ in range(T):
    N = int(input())
    if len(primes) >= N:
        print(primes[N - 1])
        continue
    for number in range(next(reversed(primes), 1) + 1, limit):
        if numbers[number]:
            primes.append(number)
            for multiple in range(number * number, limit, number):
                numbers[multiple] = False
            if len(primes) == N:
                print(number)
                break
