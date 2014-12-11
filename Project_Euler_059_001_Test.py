# Enter your code here. Read input from STDIN. Print output to STDOUT
Characters = map(int, raw_input().split(','))
Key = ""
for i in range(3):
    for j in range(97, 123):
        for k in range(i, len(Characters), 3):
            if (j ^ Characters[k] >= 97 and j ^ Characters[k] <= 122) or \
            (j ^ Characters[k] >= 65 and j ^ Characters[k] <= 90) or \
            (j ^ Characters[k] >= 48 and j ^ Characters[k] <= 57) or \
            (j ^ Characters[k] >= 39 and j ^ Characters[k] <= 41) or \
            j ^ Characters[k] == 58 or j ^ Characters[k] == 59 or \
            (j ^ Characters[k] >= 44 and j ^ Characters[k] <= 46) or \
            j ^ Characters[k] == 32 or j ^ Characters[k] == 33 or j ^ Characters[k] == 63:
                continue
            else:
                break
        else:
            Key = Key + chr(j)
            break
Sum = 0
Count = 0
for Character in Characters:
	Sum += ord(Key[Count]) ^ Character
	Count += 1
	Count %= 3
print Sum
Wait = raw_input()