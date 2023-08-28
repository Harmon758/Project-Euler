#include <stdio.h>

int main() {
    int T, N, largest, b, c, product;
    scanf("%d", &T);
    for (int _ = 0; _ < T; _++) {
        scanf("%d", &N);
        largest = -1;
        for (int a = 1; a <= N / 3; a++) {
            b = N * (a - N / 2) / (a - N);
            c = N - a - b;
            if (a * a + b * b == c * c) {
                product = a * b * c;
                if (product > largest) {
                    largest = a * b * c;
                }
            }
        }
        printf("%d\n", largest);
    }
    return 0;
}
