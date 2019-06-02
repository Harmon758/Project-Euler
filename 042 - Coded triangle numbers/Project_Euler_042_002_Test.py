Words_File = open("p042_words.txt", 'r')
Words = Words_File.read().split(',')
Word_Values = []
for i in range(len(Words)):
	Words[i] = Words[i][1:len(Words[i]) - 1]
	Word_Value = 0
	for j in range(len(Words[i])):
		Word_Value += ord(Words[i][j]) - 64
	Word_Values.append(Word_Value)
Count = 0
for i in range(len(Word_Values)):
	n = (((1 + 8 * Word_Values[i]) ** 0.5 - 1) / 2)
	if n.is_integer():
		Count += 1
print Count
Wait = raw_input()