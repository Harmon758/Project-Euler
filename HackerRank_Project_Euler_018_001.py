# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for i in range(T):
    Triangle = []
    Largest = 0
    N = int(raw_input())
    for j in range(1, N + 1):
        Triangle.append(map(int, raw_input().split()))
    for j in range(2 ** (N - 1)):
        Offset = 0
        Sum = Triangle[0][0]
        Binary = bin(j)
        Binary = Binary[2:]
        while len(Binary) < N:
            Binary = '0' + Binary
        for k in range(1, N):
            Offset += int(Binary[k])
            Sum += Triangle[k][Offset]
        if Sum > Largest:
            Largest = Sum
    print Largest