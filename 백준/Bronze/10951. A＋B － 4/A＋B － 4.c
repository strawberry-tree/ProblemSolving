#include <stdio.h>

int main(void){
    while (1){
        int a, b;
        int result = scanf("%d%d", &a, &b);
        if (result == 2) {
            printf("%d\n", a + b);
        } else {
            break;
        }
    }
    return 0;
}