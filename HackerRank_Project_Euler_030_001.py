# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
Sum = 0
for i in range(10 ** (N - 2), 9 ** N * (N - 1)):
    Sum2 = 0
    Number = i
    while Number > 0:
        Sum2 += (Number % 10) ** N
        Number = Number // 10
    if Sum2 == i:
        Sum += i
print Sum