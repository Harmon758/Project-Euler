# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
Primes = []
for i in xrange(0, int(N)):
    Primes.append(True)
for i in xrange(2, int(N / 2)):
    if Primes[i] == True:
        for j in xrange(i * i, int(N), i):
            Primes[j] = False
Primes[1] = False
Sum = 0
for i in range(N):
    j = 0
    Number = str(i)
    while j < len(str(i)):
        Number = str(i)[j:] + str(i)[:j]
        j += 1
        if not Primes[int(Number)]:
            break
    else:
        Sum += i
print Sum
        