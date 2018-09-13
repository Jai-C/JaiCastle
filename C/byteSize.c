//
//  byteSize.c
//  
//
//  Created by Jai Castle on 17/8/18.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

int main(int argc, char *argv[]){
    char prefixes[4] = " KMG";
    for (int i = 1; i < argc; i++) {
        int bytesRemaining = atoi(argv[i]);
        int n = bytesRemaining;
        int length = 0;
        while(n != 0) {
            n /= 10;
            ++length;
        }
        
        int sets;
        for (sets = 0; length > 0; sets++){
            length = length - 3;
        }
            
        if (length < 0){
            sets--;
        }
        
        while (sets > 0 && bytesRemaining != 0) {
            int currentNumber = bytesRemaining;
            for (int i = 0; i < 3*sets; i++) {
                currentNumber /= 10;
            }
            
            if (currentNumber > 0) {
                printf("%i %cBytes ", currentNumber, prefixes [sets]);
            }
            
            bytesRemaining = (bytesRemaining - currentNumber*pow(10,sets*3));
            sets--;
        }
        
        if (bytesRemaining > 0) {
            printf("%i Bytes\n", bytesRemaining);
        } else {
            printf("\n");
        }
    }
    
    return EXIT_SUCCESS;
}
