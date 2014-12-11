# Enter your code here. Read input from STDIN. Print output to STDOUT
import datetime

T = int(raw_input())
for i in range(T):
    Count = 0
    Y1, M1, D1 = map(int, raw_input().split())
    Y2, M2, D2 = map(int, raw_input().split())
    if Y1 % 10000 > Y2 % 10000:
        Y1 -= 1200
        Y2 -= 1200
    Y1 = Y1 % 10000
    Y2 = Y2 % 10000
    D1 = datetime.date(Y1, M1, D1)
    D2 = datetime.date(Y2, M2, D2)
    while D1 <= D2:
        while D1.day != 1:
            D1 += datetime.timedelta(days = 1)
        if D1.weekday() == 6:
            Count += 1
        if(D1.month == 12):
            D1 = D1.replace(year = D1.year + 1)
            D1 = D1.replace(month = 1)
        else:
            D1 = D1.replace(month = D1.month + 1)
    print Count