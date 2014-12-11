# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for i in range(T):
    N = (int(raw_input()) - 1) // 2
    print (16 * N ** 3 + 30 * N ** 2 + 26 * N + 3) // 3 % (10 ** 9 + 7)