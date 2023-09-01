i_LIMIT = 90
MODULO = 1_000_000_007

def S_k(k):
    quotient, remainder = divmod(k, 9)

    total = pow(
        10, quotient, mod = MODULO or None
    ) * (
        remainder * (remainder + 3) // 2 + 6
    ) - 9 * quotient - remainder - 6

    if MODULO:
        total %= MODULO

    return total

f = [0, 1]
while len(f) < i_LIMIT + 1:
    f.append(f[-2] + f[-1])

print(sum(S_k(f[i]) for i in range(2, i_LIMIT + 1)) % MODULO)
