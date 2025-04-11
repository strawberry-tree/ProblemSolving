#include <stdio.h>

long long calc(long long, long long);

int main(void){
    long long a, b;
    scanf("%lld%lld", &a, &b);
    printf("%lld", calc(a, b));
    return 0;
}   

long long calc(long long a, long long b){
    return (a + b) * (a - b);
}