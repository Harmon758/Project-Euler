T = int(input())
for _ in range(T):
    N = int(input())
    largest = -1
    for a in range(1, N // 3 + 1):
        b = N * (a - N // 2) // (a - N)
        c = N - a - b
        if a * a + b * b == c * c:
            product = a * b * c
            # Use := in Python 3.8
            if product > largest:
                largest = product
    print(largest)
