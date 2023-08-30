INCLUDE_AND = False
OUTPUT_1_TO_N_LETTER_COUNT = False
SCALE_LIMIT = 10 ** 12

numbers_to_words = {
    1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven",
    8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve",
    13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
    17: "Seventeen", 18: "Eighteen", 19: "Nineteen"
}

tens_digits_to_words = {
    2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy",
    8: "Eighty", 9: "Ninety"
}

short_scale_names = {
    1000: "Thousand", 1_000_000: "Million", 1_000_000_000: "Billion",
    1_000_000_000_000: "Trillion"
}

T = int(input())
for test_case in range(T):
    N = int(input())
    words = []
    for number in range(1 if OUTPUT_1_TO_N_LETTER_COUNT else N, N + 1):
        scale = SCALE_LIMIT
        while scale >= 1:
            number, scale_remainder = divmod(number, scale)
            if number:
                hundreds, hundreds_remainder = divmod(number, 100)
                if hundreds:
                    words.append(numbers_to_words[hundreds])
                    words.append("Hundred")
                    if INCLUDE_AND and hundreds_remainder:
                        words.append("And")
                if hundreds_remainder >= 20:
                    tens, hundreds_remainder = divmod(hundreds_remainder, 10)
                    words.append(tens_digits_to_words[tens])
                if hundreds_remainder:
                    words.append(numbers_to_words[hundreds_remainder])
                if scale > 1:
                    words.append(short_scale_names[scale])
            scale /= 10 ** 3
            number = scale_remainder
    if OUTPUT_1_TO_N_LETTER_COUNT:
        print(len("".join(words)))
    elif words:
        print(' '.join(words))
    else:
        print("Zero")
