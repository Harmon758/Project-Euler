# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for i in range(T):
    Number = int(raw_input())
    n = (((1 + 8 * Number) ** 0.5 - 1) / 2)
    if (n.is_integer()):
        print int(n)
    else:
        print -1