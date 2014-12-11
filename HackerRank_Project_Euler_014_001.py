# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
Lengths = []
Lengths.append(0)
Lengths.append(1)
Largest_Number = []
Largest_Number.append(0)
Largest_Number.append(1)
Largest = 0
for i in range(0, T):
    N = int(raw_input())
    for j in range(len(Largest_Number), N + 1):
        Number = j
        Count = 0
        while Number != 1 and Number >= j:
            if Number % 2 == 0:
                Number = Number / 2
            else:
                Number = 3 * Number + 1
            Count += 1
        Lengths.insert(j, Count + Lengths[Number])
        if Lengths[j] >= Largest:
            Largest = Lengths[j]
            Largest_Number.insert(j, j)
        else:
            Largest_Number.insert(j, Largest_Number[j - 1])
    print Largest_Number[N]