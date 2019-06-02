#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    long int T = 0, N = 0, Temp = 0;
    long long int Sum = 0;
    scanf("%d", &T);
    for(int i = 0; i < T; i++){
        Sum = 0;
        scanf("%d", &N);
        Temp = (N - 1) / 3;
        Sum += (Temp * (3 + Temp * 3)) / 2;
        Temp = (N - 1) / 5;
        Sum += (Temp * (5 + Temp * 5)) / 2;
        Temp = (N - 1) / 15;
        Sum -= (Temp * (15 + Temp * 15)) / 2;
        printf("%lld\n", Sum);
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
