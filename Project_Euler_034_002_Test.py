from math import factorial

N = int(raw_input())
Sum = 0
for i in range(10, N):
    Sum2 = 0
    Number = i
    while Number > 0:
        Sum2 += factorial(Number % 10)
        Number /= 10
    if Sum2 == i:
        Sum += i
print Sum
Wait = raw_input()