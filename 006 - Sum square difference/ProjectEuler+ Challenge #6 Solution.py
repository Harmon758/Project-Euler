# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for i in range(0, T):
    N = int(raw_input())
    sum_of_squares = N * (N + 1) * (2 * N + 1) / 6;
    total = N * (N + 1) / 2
    print total ** 2 - sum_of_squares