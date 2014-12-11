# Enter your code here. Read input from STDIN. Print output to STDOUT
N, K = map(int, raw_input().split())
for Number in range(2, N + 1):
    for j in range(2, K + 1):
        if sorted(str(Number * j)) != sorted(str(Number)):
            break
    else:
        for k in range(1, K + 1):
            print Number * k,
        print