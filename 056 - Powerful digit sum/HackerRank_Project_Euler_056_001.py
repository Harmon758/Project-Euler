# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
Largest = 0
for a in range(N):
    for b in range(N):
        Number = a ** b
        Sum = 0
        while Number != 0:
            Sum += Number % 10
            Number /= 10
        if Sum > Largest:
            Largest = Sum
print Largest