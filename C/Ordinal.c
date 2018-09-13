//
//  Ordinal.c
//  
//
//  Created by Jai Castle on 15/8/18.
//

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
    
    for (int i = 1; i < argc; i++) {
        int number = atoi(argv[i]);
        int lastDigit = number % 10;
        
        printf("%i", number);
        
        switch (lastDigit) {
            case 1:
                if (number != 11) {
                    printf("st");
                } else {
                    printf("th");
                }
                break;
            case 2:
                if (number != 12) {
                    printf("nd");
                } else {
                    printf("th");
                }
                break;
            case 3:
                if (number != 13) {
                    printf("rd");
                } else {
                    printf("th");
                }
                break;
            default:
                printf("th");
                break;
        }
        printf("\n");
        
    }
    
    return EXIT_SUCCESS;
}
