lengths = [0, 1]
longest = 0
longest_starting_numbers = [0, 1]

T = int(input())
for test_case in range(T):
    N = int(input())
    for starting_number in range(len(longest_starting_numbers), N + 1):
        number = starting_number
        count = 0
        while number != 1 and number >= starting_number:
            if number % 2:
                number *= 3
                number += 1
            else:
                number //= 2
            count += 1
        lengths.append(length := count + lengths[number])
        if length >= longest:
            longest = length
            longest_starting_numbers.append(starting_number)
        else:
            longest_starting_numbers.append(longest_starting_numbers[-1])
    print(longest_starting_numbers[N])
