#include <stdio.h>

int main() {
    int T, N, product;
    scanf("%d", &T);
    for (int _ = 0; _ < T; _++) {
        product = 1;
        scanf("%d", &N);
        for (int number = 2; number <= N; number++) {
            product *= number / gcd(product, number);
        }
        printf("%d\n", product);
    }
    return 0;
}

int gcd(int a, int b) {
    if (b != 0) {
        return gcd(b, a % b);
    } else {
        return a;
    }
}
