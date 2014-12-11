# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
Coins = [1, 2, 5, 10, 20, 50, 100, 200]
Count = [1] + [0]*(10 ** 5)
for Coin in Coins:
    for i in range(Coin, 10 ** 5 + 1):
        Count[i] += Count[i - Coin]
for i in range(T):
    N = int(raw_input())
    print Count[N] % (10 ** 9 + 7)