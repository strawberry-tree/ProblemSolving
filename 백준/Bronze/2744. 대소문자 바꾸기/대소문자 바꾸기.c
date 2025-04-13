#include <stdio.h>

int main(void){
    char word[150];
    gets(word);

    for (int i = 0; word[i] != '\0'; i++){
        if ('a' <= word[i] && word[i] <= 'z'){
            word[i] -= ('a' - 'A');
        } else if ('A' <= word[i] && word[i] <= 'Z'){
            word[i] += ('a' - 'A');
        }
    }

    puts(word);
    return 0;
}   
