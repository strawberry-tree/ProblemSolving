#include <stdio.h>

int main(void){
    int n, m;
    scanf("%d%d", &n, &m);
    int arrayA[n * m];
    int arrayB[n * m];

    for (int i = 0; i < n * m; i++){
        scanf("%d", &arrayA[i]);
    }
    for (int i = 0; i < n * m; i++){
        scanf("%d", &arrayB[i]);
    }

    for (int i = 0; i < n * m; i++){
        printf("%d", arrayA[i] + arrayB[i]);
        if (i % n == m - 1){
            printf("\n");
        } else{
            printf(" ");
        }
    }

    return 0;
}   
