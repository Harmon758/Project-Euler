from math import ceil, log

N_upper_bound = 10 ** 4 + 1  # 10001 (+ 1) for Project Euler Problem
limit = ceil(N_upper_bound * (log(N_upper_bound) + log(log(N_upper_bound))))

# n-th prime number < n * (log n + log log n) for n >= 6

# Rosser, Barkley.
# "Explicit Bounds for Some Functions of Prime Numbers."
# American Journal of Mathematics, vol. 63, no. 1, 1941, pp. 211-232.
# DOI: 10.2307/2371291.
# JSTOR, www.jstor.org/stable/2371291.
# Theorem 11 / Theorem 28

# Dusart, Pierre.
# "The kth prime is greater than k(log k + log log k-1) for k >= 2."
# Mathematics of Computation, vol. 68, no. 225, 1999, pp. 411-415.
# DOI: 10.1090/S0025-5718-99-01037-6.
# AMS, www.ams.org/journals/mcom/1999-68-225/S0025-5718-99-01037-6/home.html.
# JSTOR, www.jstor.org/stable/2585122.
# Lemma 1

# Unicode replaced with ASCII in citations for HackerRank:
# "[W]e don't accept submissions with non ASCII charaters [sic] for this
# challenge."

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
