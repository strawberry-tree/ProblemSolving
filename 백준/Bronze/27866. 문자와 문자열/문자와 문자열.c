#include <stdio.h>
#include <string.h>

int main(void){
    int idx;
    char s[1001];
    scanf("%s", s);
    scanf("%d", &idx);
    printf("%c", s[idx - 1]);
    return 0;
}   
