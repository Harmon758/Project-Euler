# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for i in range(T):
	N = int(raw_input())
	Flag = 0
	Largest = 0
	for j in range(999, 142, -1):
		for k in range(999, 100, -1):
			Product = j * k
			if Product < 100000:
				break
			Reverse = 0
			while Product != 0:
				Temp = Product % 10
				Reverse = Reverse * 10 + Temp
				Product /= 10
			Product = j * k
			if Product < N and Reverse == Product:
				break
		if Product > Largest:
			Largest = Product
	print Largest