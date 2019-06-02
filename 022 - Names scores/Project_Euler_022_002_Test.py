Names_File = open("p022_names.txt", 'r')
Names = Names_File.read().split(',')
for i in range(len(Names)):
	Names[i] = Names[i][1:len(Names[i]) - 1]
Names.sort()
Sum = 0
for i in range(len(Names)):
    Result = 0
    for j in range(len(Names[i])):
        Result += ord(Names[i][j]) - 64
    Sum += (i + 1) * Result
print Sum
Wait = raw_input()