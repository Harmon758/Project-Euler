# Enter your code here. Read input from STDIN. Print output to STDOUT
Intervals = [0]
i = []
for j in range(1, 19):
	Intervals.append(Intervals[j - 1] + j * (10 ** j - 10 ** (j - 1)))
for j in range(7):
	i.append(10 ** j)
Product = 1
for k in range(7):
	Interval_Index = 0
	while Intervals[Interval_Index] < i[k]:
		Interval_Index += 1
	Interval = Intervals[Interval_Index - 1]
	Quotient, Remainder = divmod(i[k] - Interval, Interval_Index)
	if Quotient % 10 == 0:
		Quotient += 10
	Number = Quotient + 10 ** (Interval_Index - 1) - 1
	Product *= int(str(Number)[Remainder - 1])
print Product
Wait = raw_input()