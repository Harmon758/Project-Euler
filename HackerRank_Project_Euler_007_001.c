#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <stdbool.h>

int main() {
    int T, N, Count;
    bool A[104744];
    scanf("%d", &T);
    for(int i = 0; i < T; i++){
        Count = 0;
        for(int j = 0; j <= 104743; j++){
            A[j] = true;
        }
        scanf("%d", &N);
        for(int j = 2; j <= sqrt(104743); j++){
            if(A[j] == true){
                for(int k = j * j; k <= 104743; k += j){
                    A[k] = false;
                }
            }
        }
        for(int j = 2; j <= 104743; j++){
            if(A[j] == true){
                Count++;
            }
            if(Count == N){
                printf("%d\n", j);
                break;
            }
        }
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
