# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

T = int(raw_input())
for i in range(T):
    Result = ""
    Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    Count = 0
    N = int(raw_input())
    N -= 1
    for j in range(0, 13):
        if N / math.factorial(13 - j - 1) == 0 or j == 12:
            Result += Letters[0]
            Letters.pop(0)
            Count += 1
        else:
            Result += Letters[N / math.factorial(13 - j - 1)]
            Letters.pop(N / math.factorial(13 - j - 1))
            N = N % math.factorial(13 - j - 1)
            Count += 1
    print Result