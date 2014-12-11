# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
Names = []
for i in range(N):
    Names.append(raw_input())
Names.sort()
Q = int(raw_input())
for i in range(Q):
    Result = 0
    Name = raw_input()
    for j in range(len(Name)):
        Result += ord(Name[j]) - 64
    print (Names.index(Name) + 1) * Result