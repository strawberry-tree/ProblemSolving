#include <stdio.h>

int main(void){
    int x, y, result;
    scanf("%d", &x);
    scanf("%d", &y);


    if (x >= 0){
        if (y >= 0){
            result = 1;
        } else {
            result = 4;
        }
    } else {
        if (y >= 0){
            result = 2;
        } else {
            result = 3;
        }
    }
    printf("%d", result);
    return 0;
}