# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import log10
from math import ceil

T = int(raw_input())
for i in range(T):
    N = int(raw_input())
    print int(ceil((N - 1 + log10(5) / 2) / log10((1 + 5 ** 0.5) / 2)))