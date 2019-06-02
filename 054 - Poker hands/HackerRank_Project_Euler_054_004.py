# Enter your code here. Read input from STDIN. Print output to STDOUT
def Sort_Numbers(Hand):
    Numbers = []
    for i in range(5):
        Numbers.append(Hand[i][0])
    for i in range(5):
        if Numbers[i] == 'T':
            Numbers[i] = 10
        elif Numbers[i] == 'J':
            Numbers[i] = 11
        elif Numbers[i] == 'Q':
            Numbers[i] = 12
        elif Numbers[i] == 'K':
            Numbers[i] = 13
        elif Numbers[i] == 'A':
            Numbers[i] = 14
        else:
            Numbers[i] = int(Numbers[i])
    Numbers.sort()
    return Numbers

def High_Card(Numbers):
    return Numbers[4]

def One_Pair(Numbers):
    if Numbers[0] == Numbers[1] != Numbers[2]:
        return [Numbers[0], Numbers[4], Numbers[3], Numbers[2]]
    elif Numbers[1] == Numbers[2] != Numbers[0] != Numbers[3]:
        return [Numbers[1], Numbers[4], Numbers[3], Numbers[0]]
    elif Numbers[2] == Numbers[3] != Numbers[1] != Numbers[4]:
        return [Numbers[2], Numbers[4], Numbers[1], Numbers[0]]
    elif Numbers[3] == Numbers[4] != Numbers[2]:
        return [Numbers[3], Numbers[2], Numbers[1], Numbers[0]]
    else:
        return 0

def Two_Pairs(Numbers):
    if Numbers[0] == Numbers[1] and Numbers[2] == Numbers[3]:
        return [Numbers[2], Numbers[0], Numbers[4]]
    elif Numbers[0] == Numbers[1] and Numbers[3] == Numbers[4]:
        return [Numbers[3], Numbers[0], Numbers[2]]
    elif  Numbers[1] == Numbers[2] and Numbers[3] == Numbers[4]:
        return [Numbers[3], Numbers[1], Numbers[0]]
    else:
        return 0

def Three_Of_A_Kind(Numbers):
    if Numbers[0] == Numbers[1] == Numbers[2] != Numbers[3]:
        return Numbers[0]
    elif Numbers[1] == Numbers[2] == Numbers[3] != Numbers[4]:
        return Numbers[1]
    elif Numbers[2] == Numbers[3] == Numbers[4] != Numbers[1]:
        return Numbers[2]
    else:
        return 0

def Straight(Numbers):
    for i in range(4):
        if Numbers[i] + 1 != Numbers[i + 1]:
            break
    else:
        return Numbers[4]
    if Numbers[0] == 2 and Numbers[1] == 3 and Numbers[2] == 4 and Numbers[3] == 5 and Numbers[4] == 14:
        return 5
    return 0

def Flush(Hand):
    Suits = []
    for i in range(5):
        Suits.append(Hand[i][1])
    if Suits[0] == Suits[1] == Suits[2] == Suits[3] == Suits[4]:
        Numbers = Sort_Numbers(Hand)
        return High_Card(Numbers)
    else:
        return 0
    
def Full_House(Numbers):
    if (Numbers[0] == Numbers[1] == Numbers[2] and Numbers[3] == Numbers[4]):
        return Numbers[0]
    elif (Numbers[0] == Numbers[1] and Numbers[2] == Numbers[3] == Numbers[4]):
        return Numbers[2]
    else:
        return 0
    
def Four_Of_A_Kind(Numbers):
    if Numbers[0] == Numbers[1] == Numbers[2] == Numbers[3] or \
    Numbers[1] == Numbers[2] == Numbers[3] == Numbers[4]:
        return Numbers[1]
    else:
        return 0
    
def Straight_Flush(Hand):
    Numbers = Sort_Numbers(Hand)
    if Straight(Numbers) != 0 and Flush(Hand) != 0:
        return Straight(Numbers)
    else:
        return 0
"""
def Royal_Flush(Hand):
    if Straight_Flush(Hand) == 14:
        return High_Card_Hand(Hand)
    else:
        return 0
"""
def Check_Hand(Hand_Type):
    def Check(Hand1, Hand2):
        if Hand_Type(Hand1) != 0 and Hand_Type(Hand2) == 0:
            return 1
        elif Hand_Type(Hand1) == 0 and Hand_Type(Hand2) != 0:
            return 2
        elif Hand_Type(Hand1) != 0 and Hand_Type(Hand2) != 0:
            if isinstance(Hand_Type(Hand1), list):
                return Check_High_Card(Hand_Type(Hand1), Hand_Type(Hand2))
            else:
                return Check_High_Card([Hand_Type(Hand1)], [Hand_Type(Hand2)])
        else:
            return 0
    return Check

def Check_High_Card(Cards1, Cards2):
    for i in range(len(Cards1)):
        if Cards1[i] > Cards2[i]:
            return 1
        elif Cards1[i] < Cards2[i]:
            return 2
    else:
        return -1

Check_Straight_Flush = Check_Hand(Straight_Flush)
Check_Four_Of_A_Kind = Check_Hand(Four_Of_A_Kind)
Check_Full_House = Check_Hand(Full_House)
Check_Flush = Check_Hand(Flush)
Check_Straight = Check_Hand(Straight)
Check_Three_Of_A_Kind = Check_Hand(Three_Of_A_Kind)
Check_Two_Pairs = Check_Hand(Two_Pairs)
Check_One_Pair = Check_Hand(One_Pair)

T = int(raw_input())
for i in range(T):
    Hands = raw_input().split()
    Hand1 = Hands[:5]
    Hand2 = Hands[5:]
    Sorted_Numbers1 = Sort_Numbers(Hand1)
    Sorted_Numbers2 = Sort_Numbers(Hand2)
    if Check_Straight_Flush(Hand1, Hand2) != 0:
        print "Player", Check_Straight_Flush(Hand1, Hand2)
    elif Check_Four_Of_A_Kind(Sorted_Numbers1, Sorted_Numbers2) != 0:
        print "Player", Check_Four_Of_A_Kind(Sorted_Numbers1, Sorted_Numbers2)
    elif Check_Full_House(Sorted_Numbers1, Sorted_Numbers2) != 0:
        print "Player", Check_Full_House(Sorted_Numbers1, Sorted_Numbers2)
    elif Check_Flush(Hand1, Hand2) != 0:
        print "Player", Check_Flush(Hand1, Hand2)
    elif Check_Straight(Sorted_Numbers1, Sorted_Numbers2) != 0:
        print "Player", Check_Straight(Sorted_Numbers1, Sorted_Numbers2)
    elif Check_Three_Of_A_Kind(Sorted_Numbers1, Sorted_Numbers2) != 0:
        print "Player", Check_Three_Of_A_Kind(Sorted_Numbers1, Sorted_Numbers2)
    elif Check_Two_Pairs(Sorted_Numbers1, Sorted_Numbers2) != 0:
        print "Player", Check_Two_Pairs(Sorted_Numbers1, Sorted_Numbers2)
    elif Check_One_Pair(Sorted_Numbers1, Sorted_Numbers2) != 0:
        print "Player", Check_One_Pair(Sorted_Numbers1, Sorted_Numbers2)
    else:
        print "Player", Check_High_Card(Sorted_Numbers1[::-1], Sorted_Numbers2[::-1])