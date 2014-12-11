# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

T = int(raw_input())
for i in range(T):
    N = int(raw_input())
    Number = math.factorial(N)
    Sum = 0
    while Number != 0:
        Sum += Number % 10
        Number /= 10
    print Sum