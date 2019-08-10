from functools import reduce
from operator import mul

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    digits = list(map(int, input()))
    max_product = product = reduce(mul, digits[:K])
    # Use math.prod in Python 3.8
    for index in range(1, N - K):
        try:
            product //= digits[index - 1]
            product *= digits[index + K - 1]
        except ZeroDivisionError:
            product = reduce(mul, digits[index:index + K])
            # Use math.prod in Python 3.8
        if product > max_product:
            max_product = product
    print(max_product)
