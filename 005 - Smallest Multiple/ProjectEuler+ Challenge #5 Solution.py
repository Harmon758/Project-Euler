def gcd(a, b):
    if b:
        return gcd(b, a % b)
    else:
        return a

T = int(input())
for _ in range(T):
    product = 1
    N = int(input())
    for number in range(2, N + 1):
        product *= number // gcd(product, number)
    print(product)
