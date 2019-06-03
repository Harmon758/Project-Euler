#include <stdio.h>

int main() {
    long int T, N;
    long int A, B, C, evens_sum;
    scanf("%ld", &T);
    for (int _ = 0; _ < T; _++) {
        scanf("%ld", &N);
        A = 1; B = 2; C = 3;
        evens_sum = 2;
        while (C < N) {
            if (C % 2 == 0) {
                evens_sum += C;
            }
            A = B; B = C; C = A + B;
        }
        printf("%ld\n", evens_sum);
    }
    return 0;
}
