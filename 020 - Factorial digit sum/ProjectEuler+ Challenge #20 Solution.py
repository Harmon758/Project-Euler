from math import factorial

T = int(input())
for test_case in range(T):
    N = int(input())
    number = factorial(N)
    sum_of_digits = 0
    while number:
        number, remainder = divmod(number, 10)
        sum_of_digits += remainder
    print(sum_of_digits)
