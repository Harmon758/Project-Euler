#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int T;
    long long N, A = 1, B = 2, C = 3, Sum = 2;
    scanf("%d", &T);
    for(int i = 0; i < T; i++){
        Sum = 2;
        A = 1;
        B = 2;
        C = 3;
        scanf("%lld", &N);
        if(N < 2){
            printf("0");
        } else{
            while(C < N){
                if(C % 2 == 0){
                    Sum += C;
                }
                A = B;
                B = C;
                C = A + B;
            }
            printf("%lld\n", Sum);
        }
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
