Numbers = range(1, 100)
Count = [1] + [0]*(100)
for Number in Numbers:
    for i in range(Number, 101):
        Count[i] += Count[i - Number]
print Count[100]
Wait = raw_input()