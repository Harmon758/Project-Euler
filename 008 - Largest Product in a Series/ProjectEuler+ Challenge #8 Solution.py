from math import prod

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    digits = list(map(int, input()))
    max_product = product = prod(digits[:K])
    for index in range(1, N - K):
        try:
            product //= digits[index - 1]
            product *= digits[index + K - 1]
        except ZeroDivisionError:
            product = prod(digits[index:index + K])
        if product > max_product:
            max_product = product
    print(max_product)
