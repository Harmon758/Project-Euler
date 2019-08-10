#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int T, N, Product = 1;
    scanf("%d", &T);
    for(int i = 0; i < T; i++){
        Product = 1;
        scanf("%d", &N);
        for(int j = 2; j <= N; j++){
            Product = Product * j / gcd(Product, j);
        }
        printf("%d\n", Product);
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}

int gcd(int a, int b){
    if(b == 0){
        return a;
    } else{
        return gcd(b, a % b);
    }
}
