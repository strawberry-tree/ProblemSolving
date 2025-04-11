#include <stdio.h>

int calc(int, int);

int main(void){
    int a, b;
    scanf("%d%d", &a, &b);
    printf("%d", calc(a, b));
    return 0;
}   

int calc(int a, int b){
    return (a + b) * (a - b);
}