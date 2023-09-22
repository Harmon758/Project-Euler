import bisect

n = 10 ** 4
m = 10 ** 16
MODULUS = 1234567891

numbers = list(range(2, n + 1))
rounds = m

while (smallest_squared := numbers[0] ** 2) < n:
    del numbers[0]
    bisect.insort(numbers, smallest_squared)
    rounds -= 1

loops, remaining_rounds = divmod(rounds, n - 1)

loops_exponent = pow(2, loops, MODULUS - 1)
loops_plus_one_exponent = loops_exponent * 2

print(
    (
        sum(
            pow(number, loops_plus_one_exponent, MODULUS)
            for number in numbers[:remaining_rounds]
        ) + 
        sum(
            pow(number, loops_exponent, MODULUS)
            for number in numbers[remaining_rounds:]
        )
    ) % MODULUS
)
