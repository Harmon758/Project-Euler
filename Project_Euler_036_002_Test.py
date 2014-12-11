N, K = map(int, raw_input().split())
Sum = 0
for Number in range(N):
    Reverse_Number = 0
    Temp_Number = Number
    while Temp_Number != 0:
        Reverse_Number = Reverse_Number * 10 + Temp_Number % 10
        Temp_Number /= 10
    if Number != Reverse_Number:
        continue
    Number_Base_K = 0
    Temp_Number = Number
    Count = 0
    while Temp_Number > 0:
        Number_Base_K += (10 ** Count) * (Temp_Number % K)
        Temp_Number /= K
        Count += 1
    Reverse_Number_Base_K = 0
    Temp_Number_Base_K = Number_Base_K
    while Temp_Number_Base_K != 0:
        Reverse_Number_Base_K = Reverse_Number_Base_K * 10 + Temp_Number_Base_K % 10
        Temp_Number_Base_K /= 10
    if Number_Base_K != Reverse_Number_Base_K:
        continue
    Sum += Number
print Sum
Wait = raw_input()