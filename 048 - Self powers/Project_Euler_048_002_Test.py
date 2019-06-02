N = int(raw_input())
Result = 1
for Number in range(2, N + 1):
    Result += pow(Number, Number, 10 ** 10)
Result %= 10 ** 10
print Result
Wait = int(raw_input())