# Enter your code here. Read input from STDIN. Print output to STDOUT
def One_Number(Number):
    if int(Number) == 1:
        print "One",
    elif int(Number) == 2:
        print "Two",
    elif int(Number) == 3:
        print "Three",
    elif int(Number) == 4:
        print "Four",
    elif int(Number) == 5:
        print "Five",
    elif int(Number) == 6:
        print "Six",
    elif int(Number) == 7:
        print "Seven",
    elif int(Number) == 8:
        print "Eight",
    elif int(Number) == 9:
        print "Nine",

def Two_Numbers(Number):
    if(int(Number) >= 20):
        if int(Number[0]) == 2:
            print "Twenty",
        elif int(Number[0]) == 3:
            print "Thirty",
        elif int(Number[0]) == 4:
            print "Forty",
        elif int(Number[0]) == 5:
            print "Fifty",
        elif int(Number[0]) == 6:
            print "Sixty",
        elif int(Number[0]) == 7:
            print "Seventy",
        elif int(Number[0]) == 8:
            print "Eighty",
        elif int(Number[0]) == 9:
            print "Ninety",
        One_Number(Number[1])
    elif(int(Number) >= 10):
        if int(Number) == 10:
            print "Ten",
        elif int(Number) == 11:
            print "Eleven",
        elif int(Number) == 12:
            print "Twelve",
        elif int(Number) == 13:
            print "Thirteen",
        elif int(Number) == 14:
            print "Fourteen",
        elif int(Number) == 15:
            print "Fifteen",
        elif int(Number) == 16:
            print "Sixteen",
        elif int(Number) == 17:
            print "Seventeen",
        elif int(Number) == 18:
            print "Eighteen",
        elif int(Number) == 19:
            print "Nineteen",
    else:
        One_Number(Number[1])

def Three_Numbers(Number):
    if(int(Number) >= 100):
        One_Number(Number[0])
        print "Hundred",
    Two_Numbers(Number[1:3])

T = int(raw_input())
for i in range (T):
    N = raw_input()
    while len(N) < 12:
        N = '0' + N
    if int(N[0:3]) != 0:
        Three_Numbers(N[0:3])
        print "Billion",
    if int(N[3:6]) != 0:
        Three_Numbers(N[3:6])
        print "Million",
    if int(N[6:9]) != 0:
        Three_Numbers(N[6:9])
        print "Thousand",
    if int(N[9:12]) != 0:
        Three_Numbers(N[9:12])
    if int(N) == 0:
        print "Zero"
    if int(N) == 10 ** 12:
        print "One Trillion"
    print