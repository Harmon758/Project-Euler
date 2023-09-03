import datetime

T = int(input())
for test_case in range(T):
    Y_1, M_1, D_1 = map(int, input().split())
    Y_2, M_2, D_2 = map(int, input().split())

    Y_difference = Y_2 - Y_1
    Y_1 %= 400
    Y_1 += 400
    Y_2 = Y_1 + Y_difference

    first_of_the_month_sunday_count = 0

    if D_1 == 1:
        date = datetime.date(Y_1, M_1, 1)
    elif M_1 == 12:
        date = datetime.date(Y_1 + 1, 1, 1)
    else:
        date = datetime.date(Y_1, M_1 + 1, 1)

    while date <= datetime.date(Y_2, M_2, D_2):
        if date.isoweekday() == 7:
            first_of_the_month_sunday_count += 1
        if date.month == 12:
            date = date.replace(year = date.year + 1, month = 1)
        else:
            date = date.replace(month = date.month + 1)

    print(first_of_the_month_sunday_count)
