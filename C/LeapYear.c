//
//  LeapYear.c
//  
//
//  Created by Jai Castle on 15/8/18.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main(int argc, char *argv[]){
    
    if (argc == 2) {
        int year = atoi(argv[1]);
        bool leapYear = false;
        if (year % 400 == 0) {
            leapYear = true;
        } else {
            leapYear = (year % 4 == 0) && (year % 100 != 0);
        }
        if (leapYear) {
            printf("Leap year\n");
        } else {
            printf("Not a leap year\n");
        }
        
    } else {
        printf("Please enter 1 argument\n");
    }
    
    return EXIT_SUCCESS;
}
