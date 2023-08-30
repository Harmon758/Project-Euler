from math import sqrt

MODULO = 10 ** 9 + 7

K = int(input())
max_sum = K * 9 ** 2 + 1

unhappiness = {0: False, 1: False, 89: True}
for number in range(2, max_sum):
    if number in unhappiness:
        continue
    chain = []
    unhappy = None
    while unhappy is None:
        chain.append(number)
        sum_of_digits_squared = 0
        while number:
            number, remainder = divmod(number, 10)
            sum_of_digits_squared += remainder * remainder
        number = sum_of_digits_squared
        unhappy = unhappiness.get(number)
    for chain_number in chain:
        unhappiness[chain_number] = unhappy

sum_numbers_counts = [0] * max_sum
for digit in range(10):
    sum_numbers_counts[digit * digit] = 1
updated_sum_numbers_counts = [0] * max_sum
for digit in range(2, K + 1):
    for digits_squared_sum in range(min(81, max_sum)):
        updated_sum_numbers_counts[digits_squared_sum] = sum(
            sum_numbers_counts[digits_squared_sum - digit * digit]
            for digit in range(int(sqrt(digits_squared_sum)) + 1)
        )
        if MODULO:
            updated_sum_numbers_counts[digits_squared_sum] %= MODULO
    for digits_squared_sum in range(81, max_sum):
        updated_sum_numbers_counts[digits_squared_sum] = sum(
            sum_numbers_counts[digits_squared_sum - digit * digit]
            for digit in range(10)
        )
        if MODULO:
            updated_sum_numbers_counts[digits_squared_sum] %= MODULO
    sum_numbers_counts = updated_sum_numbers_counts.copy()

unhappy_count = sum(
    sum_numbers_counts[digits_squared_sum]
    for digits_squared_sum in range(max_sum)
    if unhappiness[digits_squared_sum]
)
print(unhappy_count % MODULO if MODULO else unhappy_count)
