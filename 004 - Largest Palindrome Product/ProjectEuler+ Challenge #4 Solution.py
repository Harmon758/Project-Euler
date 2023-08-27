T = int(input())
for _ in range(T):
    N = int(input())
    largest = 0
    limit = N - 1
    for number_1 in range(999, 100, -1):
        if number_1 % 11:
            start = min(990, limit // number_1 // 11 * 11)
            step = -11
        else:
            start = min(999, limit // number_1)
            step = -1
        for number_2 in range(start, number_1, step):
            product = number_1 * number_2
            if product <= largest:
                break
            product_str = str(product)
            if product_str == product_str[::-1]:
                largest = product
                break
    print(largest)
