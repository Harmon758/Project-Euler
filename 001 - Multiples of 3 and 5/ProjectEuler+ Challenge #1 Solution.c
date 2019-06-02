#include <stdio.h>

int main() {
    long int T = 0, N = 0;
    long int multiples_of_3 = 0, multiples_of_5 = 0, multiples_of_15 = 0;
    long long int sum = 0;
    scanf("%ld", &T);
    for (int _ = 0; _ < T; _++) {
        scanf("%ld", &N);
        multiples_of_3 = (N - 1) / 3;
        multiples_of_5 = (N - 1) / 5;
        multiples_of_15 = (N - 1) / 15;
        sum = 3 * multiples_of_3 * (multiples_of_3 + 1) / 2
              + 5 * multiples_of_5 * (multiples_of_5 + 1) / 2
              - 15 * multiples_of_15 * (multiples_of_15 + 1) / 2;
        printf("%lld\n", sum);
    }  
    return 0;
}
