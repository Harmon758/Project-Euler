T = int(input())
for test_case in range(T):
    N = int(input())
    number = 2 ** N
    sum_of_digits = 0
    while number:
        number, digit = divmod(number, 10)
        sum_of_digits += digit
    print(sum_of_digits)
