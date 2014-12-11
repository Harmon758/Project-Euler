# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
Product = 1
for i in range(0, N):
    Product += int(raw_input())
print str(Product)[0:10]