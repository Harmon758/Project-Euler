from itertools import cycle

n_S = 10 ** 14
modulus = 123454321

sequence = cycle((1, 2, 3, 4, 3, 2))
v = []
prefixes = []
for n_v in range(30):
    digits = []
    while sum(digits) != n_v + 1:
        digits.append(next(sequence))
    v_n = sum(
        digit * 10 ** magnitude
        for magnitude, digit in enumerate(reversed(digits))
    )
    if n_v < 15:
        v.append(v_n)
    else:
        prefixes.append(v_n - v[n_v % 15])

# v = [
#     1, 2, 3, 4, 32, 123, 43, 2123, 432, 1234, 32123, 43212, 34321, 23432,
#     123432
# ]

# prefixes = [
#     1234320, 2343210, 3432120, 4321230, 32123400, 123432000, 43212300,
#     2123430000, 432123000, 1234320000, 32123400000, 43212300000, 34321200000,
#     23432100000, 123432000000
# ]

cycles, partial_cycle = divmod(n_S, 15)
ratio = 10 ** 6

magnitude = pow(ratio, cycles, modulus)
modular_inverse = pow(ratio - 1, -1, modulus)

print(
    (
        cycles * sum(v) + sum(prefixes) * (
            (magnitude - cycles * (ratio - 1) - 1) * modular_inverse ** 2
        ) + sum(v[:partial_cycle]) + sum(prefixes[:partial_cycle]) * (
            (magnitude - 1) * modular_inverse
        )
    ) % modulus
)
