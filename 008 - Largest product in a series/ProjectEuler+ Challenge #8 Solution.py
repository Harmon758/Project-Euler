# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for i in range (0, T):
    N, K = map(int, raw_input().split())
    Number = int(raw_input())
    Max_Product = 0
    for j in range(0, N - K):
        Product = 1
        for k in range(j, j + K):
            Product *= int(str(Number)[k - 1])
        if Product > Max_Product:
            Max_Product = Product
    print Max_Product