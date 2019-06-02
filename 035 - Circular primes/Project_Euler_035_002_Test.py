N = int(raw_input())
Primes = [True]*N
for i in xrange(2, int(N ** 0.5)):
    if Primes[i] == True:
        for j in xrange(i * i, int(N), i):
            Primes[j] = False
Primes[0] = Primes[1] = False
Count = 0
for i in range(N):
    j = 0
    Number = str(i)
    while j < len(str(i)):
        Number = str(i)[j:] + str(i)[:j]
        j += 1
        if not Primes[int(Number)]:
            break
    else:
        Count += 1
print Count
Wait = raw_input()        