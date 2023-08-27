#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

int main() {
    int N_upper_bound = 10001;  // 10001 (+ 1) for Project Euler Problem
    long int limit = ceil(N_upper_bound *
                          (log(N_upper_bound) + log(log(N_upper_bound))));

    // n-th prime number < n * (log n + log log n) for n >= 6

    /*
    Rosser, Barkley
    "Explicit Bounds for Some Functions of Prime Numbers"
    American Journal of Mathematics, vol. 63, no. 1, 1941, pp. 211-232
    DOI: 10.2307/2371291
    JSTOR, www.jstor.org/stable/2371291
    Theorem 11 / Theorem 28
    */

    /*
    Dusart, Pierre
    "The kth prime is greater than k(log k + log log k-1) for k >= 2"
    Mathematics of Computation, vol. 68, no. 225, 1999, pp. 411-415
    DOI: 10.1090/S0025-5718-99-01037-6
    AMS, www.ams.org/journals/mcom/1999-68-225/S0025-5718-99-01037-6/home.html
    JSTOR, www.jstor.org/stable/2585122
    Lemma 1
    */

    /*
    Unicode replaced with ASCII in citations for HackerRank:
    "[W]e don't accept submissions with non ASCII charaters [sic] for this
    challenge."
    */

    bool numbers[++limit];
    memset(numbers, true, (limit) * sizeof(bool));
    long int primes[N_upper_bound];
    int primes_count = 0;

    int T, N;
    scanf("%d", &T);
    for (int _ = 0; _ < T; _++) {
        scanf("%d", &N);
        if (primes_count >= N) {
            printf("%ld\n", primes[N - 1]);
            continue;
        }
        long int number = 2;
        if (primes_count != 0) {
            number = primes[primes_count - 1] + 1;
        }
        for (; number < limit; number++) {
            if (numbers[number]) {
                primes[primes_count++] = number;
                for (long int multiple = number * number; multiple < limit;
                     multiple += number) {
                    numbers[multiple] = false;
                }
                if (primes_count == N) {
                    printf("%ld\n", number);
                    break;
                }
            }
        }
    }
    return 0;
}
