#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int T, N, Largest, l, k;
    scanf("%d", &T);
    for(int i = 0; i < T; i++){
        scanf("%d", &N);
        Largest = 0;
        for(int j = 1; j <= N / 3; j++){
            k = (2 * j * N - N * N) / (2 * j - 2 * N);
            l = N - k - j;
            if(l * l == k * k +  j * j && l * k * j > Largest){
                Largest = l * k * j;
            }
        }
        if(Largest == 0){
            printf("-1\n");
        } else{
            printf("%d\n", Largest);
        }
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
