T = int(input())
for _ in range(T):
    N = int(input())
    square_of_sum = (N * (N + 1) // 2) ** 2
    sum_of_squares = N * (N + 1) * (2 * N + 1) // 6
    print(square_of_sum - sum_of_squares)
