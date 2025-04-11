#include <stdio.h>

int main(void){
    int year, result;
    scanf("%d", &year);

    if (year % 4 == 0){
        if (year % 100 == 0){
            if (year % 400 == 0){
                result = 1;
            } else {
                result = 0;
            }
        } else {
            result = 1;
        }
    } else {
        result = 0;
    }

    printf("%d", result);
    
    return 0;
}