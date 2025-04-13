#include <stdio.h>

int main(void){
    int checked[31] = {0};
    int index;
    int found;
    int count = 0;

    for (int i = 0; i < 28; i++){
        scanf("%d", &index);
        checked[index] = 1;
    }

    for (int num = 1; num < 31; num++){
        if (checked[num] == 0){
            printf("%d\n", num);
            count++;
            if (count == 2){
                break;
            }
        }
    }

    return 0;
}   
