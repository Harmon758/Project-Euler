from collections import Counter
from functools import reduce
from itertools import combinations_with_replacement
from math import factorial
from operator import mul

arrives_at_89 = {0: False, 1: False, 89: True}
for number in range(2, 7 * 9 ** 2 + 1):
    if number in arrives_at_89:
        continue
    chain = []
    number_arrives_at_89 = None
    while number_arrives_at_89 is None:
        chain.append(number)
        number = sum(int(digit) ** 2 for digit in str(number))
        number_arrives_at_89 = arrives_at_89.get(number)
    for chain_number in chain:
        arrives_at_89[chain_number] = number_arrives_at_89

factorials = [factorial(number) for number in range(8)]

count = 0
for number in combinations_with_replacement(range(10), 7):
    if arrives_at_89[sum(digit ** 2 for digit in number)]:
        # Use math.prod in Python 3.8
        count += (factorials[7] //
                  reduce(mul, [factorials[c]
                               for c in Counter(number).values()]))
print(count)
