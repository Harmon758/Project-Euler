def One_Number(Number):
    if int(Number) == 1:
        return "One"
    elif int(Number) == 2:
        return "Two"
    elif int(Number) == 3:
        return "Three"
    elif int(Number) == 4:
        return "Four"
    elif int(Number) == 5:
        return "Five"
    elif int(Number) == 6:
        return "Six"
    elif int(Number) == 7:
        return "Seven"
    elif int(Number) == 8:
        return "Eight"
    elif int(Number) == 9:
        return "Nine"
    else:
        return ""

def Two_Numbers(Number):
    if(int(Number) >= 20):
        if int(Number[0]) == 2:
            return "Twenty" + One_Number(Number[1])
        elif int(Number[0]) == 3:
            return "Thirty" + One_Number(Number[1])
        elif int(Number[0]) == 4:
            return "Forty" + One_Number(Number[1])
        elif int(Number[0]) == 5:
            return "Fifty" + One_Number(Number[1])
        elif int(Number[0]) == 6:
            return "Sixty" + One_Number(Number[1])
        elif int(Number[0]) == 7:
            return "Seventy" + One_Number(Number[1])
        elif int(Number[0]) == 8:
            return "Eighty" + One_Number(Number[1])
        elif int(Number[0]) == 9:
            return "Ninety" + One_Number(Number[1])
    elif(int(Number) >= 10):
        if int(Number) == 10:
            return "Ten"
        elif int(Number) == 11:
            return "Eleven"
        elif int(Number) == 12:
            return "Twelve"
        elif int(Number) == 13:
            return "Thirteen"
        elif int(Number) == 14:
            return "Fourteen"
        elif int(Number) == 15:
            return "Fifteen"
        elif int(Number) == 16:
            return "Sixteen"
        elif int(Number) == 17:
            return "Seventeen"
        elif int(Number) == 18:
            return "Eighteen"
        elif int(Number) == 19:
            return "Nineteen"
    else:
        return One_Number(Number[1])

def Three_Numbers(Number):
    if int(Number) % 100 == 0:
        return One_Number(Number[0]) + "Hundred"
    elif int(Number) >= 100:
        return One_Number(Number[0]) + "Hundredand" + Two_Numbers(Number[1:3])
    else:
        return Two_Numbers(Number[1:3])

Numbers = ""
for i in range(1, 1001):
    str_i = str(i)
    if len(str_i) == 4:
        Numbers += "OneThousand"
    else:
        while len(str_i) < 3:
            str_i = '0' + str_i
        Numbers += Three_Numbers(str_i)
print len(Numbers)
Wait = int(raw_input())