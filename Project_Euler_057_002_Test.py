N = int(raw_input())
Numerator = 3
Denominator = 2
Count = 0
for i in range(2, N + 1):
    Numerator, Denominator = Numerator + 2 * Denominator, Numerator + Denominator
    if len(str(Numerator)) > len(str(Denominator)):
        Count += 1
print Count
Wait = raw_input()