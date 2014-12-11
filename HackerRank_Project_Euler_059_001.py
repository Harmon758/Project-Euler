# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
Characters = map(int, raw_input().split())
Key = ""
for i in range(3):
    for j in range(97, 123):
        for k in range(i, N, 3):
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
print Key
