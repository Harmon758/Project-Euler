T = int(input())
for _ in range(T):
    N = int(input())
    A, B, C = 1, 2, 3
    evens_sum = 2
    while C < N:
        if not C % 2:
            evens_sum += C
        A, B, C = B, C, B + C
    print(evens_sum)
