from math import sqrt

mod = 10 ** 9 + 7
K = int(input())
sum_limit = K * 9 ** 2 + 1

arrives_at_89 = {0: False, 1: False, 89: True}
for number in range(2, sum_limit):
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

counts = [0] * sum_limit
for digit in range(10):
    counts[digit * digit] = 1
new = [0] * (sum_limit)
for _ in range(2, K + 1):
    for n in range(min(81, sum_limit)):
        new[n] = sum(counts[n - d * d] for d in range(int(sqrt(n)) + 1)) % mod
    for n in range(81, sum_limit):
        new[n] = sum(counts[n - d * d] for d in range(10)) % mod
    counts = new.copy()
count = sum(counts[n] for n in range(sum_limit) if arrives_at_89[n])
print(count % mod)
