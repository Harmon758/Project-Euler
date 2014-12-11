# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import factorial

def perm(n, s):
    """
    requires function factorial()
    Find the nth permutation of the string s. Example:

    >>>perm(30, 'abcde')
    bcade
    """
    if len(s)==1: return s
    q, r = divmod(n, factorial(len(s) - 1))
    return s[q] + perm(r, s[:q] + s[q + 1:])

N = int(raw_input())
Numbers = "0123456789"
Sum = 0
for i in xrange(factorial(N + 1)):
    Str_i = perm(i, Numbers[:N + 1])
    if not Numbers[:N + 1].strip(Str_i):
        if len(Str_i) == 10 and int(Str_i[7:10]) % 17 != 0:
            continue
        if len(Str_i) >= 9 and int(Str_i[6:9]) % 13 != 0:
            continue
        if len(Str_i) >= 8 and int(Str_i[5:8]) % 11 != 0:
            continue
        if len(Str_i) >= 7 and int(Str_i[4:7]) % 7 != 0:
            continue
        if len(Str_i) >= 6 and int(Str_i[3:6]) % 5 != 0:
            continue
        if len(Str_i) >= 5 and int(Str_i[2:5]) % 3 != 0:
            continue
        if int(Str_i[1:4]) % 2 != 0:
            continue
        Sum += int(Str_i)
print Sum
Wait = raw_input()

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
if N == 3:
    print 22212
elif N == 4:
    print 711104
elif N == 5:
    print 12444480
elif N == 6:
    print 189838560
elif N == 7:
    print 1099210170
elif N == 8:
    print 1113342912
elif N == 9:
	print 16695334890
"""