# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

T = int(raw_input())
for i in range(T):
    Result = ""
    Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    N = int(raw_input())
    N -= 1
    for j in range(0, 13):
        if N / math.factorial(12 - j) == 0:
            Result += Letters[0]
            Letters.pop(0)
        else:
            Result += Letters[N / math.factorial(12 - j)]
            Letters.pop(N / math.factorial(12 - j))
            N = N % math.factorial(12 - j)
    print Result