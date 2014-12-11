#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int T, N, Product = 0, Flag = 0, Reverse = 0, Temp = 1, Largest = 0;
    scanf("%d", &T);
    for(int i = 0; i < T; i++){
        scanf("%d", &N);
        Flag = 0;
        Largest = 0;
        for(int j = 999; j > 142; j--){
            for(int k = 999; k > 100; k--){
                Product = j * k;
                if(Product < 100000){
                    break;
                }
                Reverse = 0;
                while(Product != 0){
                    Temp = Product % 10;
                    Reverse = Reverse * 10 + Temp;
                    Product = Product / 10;
                }
                Product = j * k;
                if(Product < N && Reverse == Product){
                    break;
                }
            }
            if(Product > Largest){
                Largest = Product;
            }
        }
        printf("%d\n", Largest);
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}