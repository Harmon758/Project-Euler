from math import isqrt

N = 10 ** 12

def S_number_check(sqrt_value, digits):
    if digits < sqrt_value:
        return False
    if digits == sqrt_value:
        return True

    magnitude = 10
    while magnitude < digits:
        remaining_digits, split_digits = divmod(digits, magnitude)
        if split_digits >= sqrt_value:
            return False
        if S_number_check(sqrt_value - split_digits, remaining_digits):
            return True
        magnitude *= 10

    return False

print(
    sum(
        n
        for multiple_of_9 in range(9, isqrt(N) + 1, 9)
        for sqrt_n in range(multiple_of_9, multiple_of_9 + 2)
        if S_number_check(sqrt_n, n := sqrt_n * sqrt_n)
    )
)
