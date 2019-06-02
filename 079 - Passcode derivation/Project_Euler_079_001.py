Keylog = open("p079_keylog.txt", 'r')
Keys = []
for Line in Keylog.readlines():
	Keys.append(str(Line[:len(Line) - 1]))
Numbers_After = {}
Numbers = set()
Passcode = ""
for i in range(10):
	Numbers_After[i] = set()
for Key in Keys:
	for Digit in range(len(Key)):
		Numbers.add(int(Key[Digit]))
		for Digit_After in range(Digit + 1, len(Key)):
			Numbers_After[int(Key[Digit])].add(int(Key[Digit_After]))
while Numbers:
	for Number in Numbers:
		if not Numbers_After[Number]:
			Passcode = str(Number) + Passcode
			for i in range(10):
				Numbers_After[i].discard(Number)
			Numbers.remove(Number)
			break
print Passcode
Wait = raw_input()