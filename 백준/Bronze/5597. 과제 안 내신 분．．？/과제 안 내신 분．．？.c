#include <stdio.h>

int main(void){
    int submitted[28];
    int found;
    int count = 0;

    for (int i = 0; i < 28; i++){
        scanf("%d", &submitted[i]);
    }

    for (int num = 1; num < 31; num++){
        found = 0;
        for (int i = 0; i < 28; i++){
            if (submitted[i] == num){
                found = 1;
                break;
            }
        }
        if (found == 0){
            printf("%d\n", num);
            count++;
            if (count >= 2){
                break;
            }
        }
    }

    return 0;
}   
