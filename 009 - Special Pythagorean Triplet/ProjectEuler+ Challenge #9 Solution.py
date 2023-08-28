T = int(input())
for _ in range(T):
    N = int(input())
    largest = -1
    for a in range(1, N // 3 + 1):
        b = N * (a - N // 2) // (a - N)
        c = N - a - b
        if a * a + b * b == c * c and (product := a * b * c) > largest:
            largest = product
    print(largest)
