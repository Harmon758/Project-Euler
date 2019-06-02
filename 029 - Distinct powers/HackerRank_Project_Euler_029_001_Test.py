# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
print len({a ** b for a in range(2, N + 1) for b in range(2, N + 1)})