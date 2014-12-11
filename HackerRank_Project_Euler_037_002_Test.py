# Enter your code here. Read input from STDIN. Print output to STDOUT
A = [True]*(10 ** 6)
for j in xrange(2, 10 ** 3):
    if A[j] == True:
        for k in xrange(j * j, 10 ** 6, j):
            A[k] = False
A[1] = False
N = int(raw_input())
Flag = False
Sum = 0
for Number in range(11, N):
    Flag = False
    Temp_Number = Number
    while Temp_Number > 0:
        if not A[Temp_Number]:
            Flag = True
            break
        Temp_Number /= 10
    if Flag:
        continue
    Temp_Number = Number
    for j in range(len(str(Temp_Number)), 0, -1):
        if not A[Temp_Number]:
            Flag = True
            break
        Temp_Number %= 10 ** (j - 1)
    if Flag:
        continue
    Sum += Number
print Sum