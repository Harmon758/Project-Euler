# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import factorial

T = int(raw_input())
for i in range(T):
    Result = ""
    Letters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    N = int(raw_input())
    N -= 1
    for j in range(0, 10):
        if N / factorial(9 - j) == 0:
            Result += Letters[0]
            Letters.pop(0)
        else:
            Result += Letters[N / factorial(9 - j)]
            Letters.pop(N / factorial(9 - j))
            N = N % factorial(9 - j)
    print Result