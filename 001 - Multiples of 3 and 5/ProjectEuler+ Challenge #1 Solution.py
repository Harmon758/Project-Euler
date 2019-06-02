T = int(input())
for _ in range(T):
    N = int(input())
    multiples_of_3 = (N - 1) // 3
    multiples_of_5 = (N - 1) // 5
    multiples_of_15 = (N - 1) // 15
    sum = (3 * multiples_of_3 * (multiples_of_3 + 1) // 2
           + 5 * multiples_of_5 * (multiples_of_5 + 1) // 2
           - 15 * multiples_of_15 * (multiples_of_15 + 1) // 2)
    print(sum)
