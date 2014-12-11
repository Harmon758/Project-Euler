# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for i in range(T):
    N = int(raw_input())
    Sum = 0
    Number = 2 ** N
    while Number != 0:
        Sum += Number % 10
        Number /= 10
    print Sum