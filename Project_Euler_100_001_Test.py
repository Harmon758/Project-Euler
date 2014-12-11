Total = 10 ** 12
Red = int((Total * (Total - 1) / 2) ** 0.5)
Blue = Red + 1
while Red * Blue * 2 != Total * (Total - 1):
	Total += 1
	Red = int((Total * (Total - 1) / 2) ** 0.5)
	Blue = Red + 1
print Blue
Wait = raw_input()