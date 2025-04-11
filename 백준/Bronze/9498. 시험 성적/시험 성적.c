#include <stdio.h>

int main(void){
    int score;
    char result;
    scanf("%d", &score);
    
    if (score >= 90){
        result = 'A';
    } else if (score >= 80){
        result = 'B';
    } else if (score >= 70){
        result = 'C';
    } else if (score >= 60){
        result = 'D';
    } else {
        result = 'F';
    }

    printf("%c\n", result);
    return 0;
}