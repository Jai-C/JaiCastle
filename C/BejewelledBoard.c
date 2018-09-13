//
//  Workshop4.c
//  
//
//  Created by Jai Castle on 23/8/18.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define     N   6

#define     FOREACH_COL         for (int i = 0; i < N; i++)
#define     FOREACH_ROW         for (int j = 0; j < N; j++)
#define     FOREACH_ADJACENT    for (int i = -1; i <= 1; i++)

char board[N][N];
char colors[5] = {'R', 'G', 'B', 'Y', ' '};

void reset(void){
     FOREACH_COL {
        FOREACH_ROW {
            int randomColor = (rand() % 4);
            board[i][j] = colors[randomColor];
        }
    }
}

bool valid(int col, int row){
    return col < N && col >= 0 && row < N && row >=0;
}

int clearColors(int col, int row, char want){
    int removed = 0;
    
    if (valid(col, row) && board[col][row] == want){
        board[col][row] = ' '; // Stop infinite loop
        return  1   + clearColors(col-1,row,want)
                    + clearColors(col, row-1, want)
                    + clearColors(col+1,row,want)
                    + clearColors(col, row+1, want);
    }
    
    return removed;
}

int click(int col, int row){
    if (valid(col, row)) {
        return 0;
    } else if (board[col][row] == ' '){
        return 0;
    }
    
    int removed = clearColors(col, row, board[col][row]);
    
    FOREACH_COL {
        FOREACH_ROW {
            if (valid(i,j-1)){
                if (board[i][j-1] == ' '){
                    board[i][j-1] = board[i][j];
                    board[i][j] = ' ';
                }
            }
        }
    }
    
    return removed * removed;
}

int main(int argc, char *argv[]){
    
    // CODE HERE
    reset();
    
    return EXIT_SUCCESS;
}
