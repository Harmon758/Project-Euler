# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
Pandigital_Products = set()
Numbers = "123456789"
for i in range(2, 80):
    for j in range(2, 10000 / i):
        if len(str(i) + str(j) + str(i * j)) == N and not Numbers[:N].strip(str(i) + str(j) + str(i * j)):
            Pandigital_Products.add(i * j)
print sum(Pandigital_Products)