# Enter your code here. Read input from STDIN. Print output to STDOUT
def Reverse(Number):
	Reverse = 0
	while Number != 0:
		Temp = Number % 10
		Reverse = Reverse * 10 + Temp
		Number /= 10
	return Reverse

N = int(raw_input())
Palindromes = {}
for i in range(10, N):
	Number = i
	Reverse_Number = Reverse(Number)
	Count = 0
	while Reverse_Number != Number:
		Number += Reverse_Number
		Reverse_Number = Reverse(Number)
		Count += 1
		if Count == 60:
			break
	if Count == 60:
		continue
	if Number in Palindromes:
		Palindromes[Number] += 1
	else:
		Palindromes[Number] = 1
Most = 0
Most_Palindrome = 0
for Palindrome in Palindromes:
	if Palindromes[Palindrome] > Most:
		Most_Palindrome = Palindrome
		Most = Palindromes[Palindrome]
print Most_Palindrome, Most