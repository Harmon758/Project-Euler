# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
Numerator = 3
Denominator = 2
for i in range(2, N + 1):
    Numerator, Denominator = Numerator + 2 * Denominator, Numerator + Denominator
    if len(str(Numerator)) > len(str(Denominator)):
        print i