#include <stdio.h>

int main() {
    int T, N, largest, limit, start, step, temp, product, reverse;
    scanf("%d", &T);
    for (int _ = 0; _ < T; _++) {
        scanf("%d", &N);
        largest = 0;
        limit = N - 1;
        for (int num_1 = 999; num_1 > 100; num_1--) {
            if (num_1 % 11 != 0) {
                temp = limit / num_1 / 11 * 11;
                start = 990 < temp ? 990 : temp;
                step = -11;
            } else {
                temp = limit / num_1;
                start = 999 < temp ? 999 : temp;
                step = -1;
            }
            for (int num_2 = start; num_2 > num_1; num_2 += step) {
                product = num_1 * num_2;
                if (product <= largest) {
                    break;
                }
                reverse = 0;
                temp = product;
                while (temp != 0) {
                    reverse *= 10;
                    reverse += temp % 10;
                    temp /= 10;
                }
                if (reverse == product) {
                    largest = product;
                    break;
                }
            }
        }
        printf("%d\n", largest);
    }
    return 0;
}
