#include <stdio.h>

int main(void){
    int result = 1;
    int n;
    scanf("%d", &n);

    for (int i = 2; i <= n; i++){
        result *= i;
    }
    printf("%d", result);
    return 0;
}