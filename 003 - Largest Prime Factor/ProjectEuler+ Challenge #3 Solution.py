T = int(input())
for _ in range(T):
    N = number = int(input())
    largest = 2
    while not number % 2:
        number //= 2
    factor = 3
    max_factor = number ** 0.5
    while factor <= max_factor:
        if not number % factor:
            largest = factor
            number //= factor
            while not number % factor:
                number //= factor
            if number == 1:
                print(largest)
                break
            max_factor = number ** 0.5
        factor += 2
    else:
        print(number)
