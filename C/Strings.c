//
//  Lab3.c
//  
//
//  Created by Jai Castle on 22/8/18.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>
#include <string.h>

int my_strlen(char s[]){
    return strlen(s);
    int length;
    for(length = 0; s[length] != '\0'; length++);
    
    return length;
}

bool isVowel(char c){
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int numberOfVowels(char s[]){
    int length = my_strlen(s);
    int vowels = 0;
    for (int i = 0; i < length; i++) {
        if (isVowel(s[i])){
            vowels++;
        }
    }
    return vowels;
}

bool isSafe(char s[]) {
    int length = my_strlen(s);
    int lowerCase = 0;
    int upperCase = 0;
    int digits = 0;
    for (int i = 0; i < length; i++) {
        char c = s[i];
        if (isupper(c)) {
            upperCase++;
        } else if (islower(c)){
            lowerCase++;
        } else if (!isalpha(c)){
            digits++;
        }
    }
    
    return lowerCase >= 2 && upperCase >= 2 && digits >= 2;
}

int my_strcmp(char s1[], char s2[]){
    int length1 = my_strlen(s1);
    int length2 = my_strlen(s2);
    
    if (length1 > length2) {
        return 1;
    } else if (length2 > length1){
        return -1;
    }
    
    for (int i = 0; i < length1; i++) {
        if (s1[i] != s2[i]) {
            return -1;
        }
    }
    
    return 0;
}

bool isPalindrome(char s[]){
    int length = my_strlen(s);
    for (int i = 0; i < length/2; i++) {
        if (s[i] != s[length-1-i]) {
            return false;
        }
    }
    return true;
}



int main(int argc, char *argv[]){
    printf("%i\n", my_strlen(argv[1]));
    printf("%i\n", numberOfVowels(argv[2]));
    printf("%i\n", isSafe(argv[3]));
    printf("%i\n", my_strcmp(argv[4], argv[5]));
    printf("%i\n", isPalindrome(argv[6]));
    
    return EXIT_SUCCESS;
}
