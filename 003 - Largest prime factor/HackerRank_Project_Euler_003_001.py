# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for i in range(0, T):
    Largest = 0
    N = int(raw_input())
    Factor = N
    while Factor != 1:
        for j in xrange(2, int(Factor ** 0.5 + 1)):
            if Factor % j == 0:
                Largest = j
                Factor = Factor / j
                break;
        else:
            Largest = Factor
            break;
    print Largest