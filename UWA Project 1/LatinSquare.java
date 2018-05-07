/**
 * Some weird class to do unnecessary stuff
 *
 * @author Jai Castle
 * @version 30 April 2018
 */
public class LatinSquare
{
    // returns true iff n is in the xth row of a
    // e.g. inRow(4, {{3, 5}, {3, 6, 4}, {2}}, 1) = true, 
    // e.g. inRow(4, {{3, 5}, {3, 6, 4}, {2}}, 2) = false
    public static boolean inRow(int n, int[][]a, int x)
    {
        for (int element: a[x]){
            if (element == n){
                return true;
            }
        }
        return false;
    }

    // returns true iff n is in the xth column of a
    // e.g. inColumn(4, {{3, 5}, {3, 6, 4}, {2}}, 2) = true, 
    // e.g. inColumn(4, {{3, 5}, {3, 6, 4}, {2}}, 1) = false
    public static boolean inColumn(int n, int[][]a, int x)
    {
        for (int[] array: a){
            if (x < array.length && n == array[x]){
                return true;
            }
        }
        return false;
    }

    // returns true iff a is a Latin Square containing the numbers 1..n 
    // a must be a square of side n, and every row and every column must be a permutation of 1..n
    // http://en.wikipedia.org/wiki/Latin_square
    public static boolean isLatin(int[][] a)
    {
        if (LabWeek9.isSquare(a) == false){
            System.out.println("Not square");
            return false;
        }
        
        int max = a[0].length;
        for (int i = 0; i < max; i++){
            for (int j = 1; j <= max; j++){
                if (!inColumn(j,a,i)){
                    return false;
                }
            }
        }
        
        for (int i = 0; i < max; i++){
            for (int j = 1; j <= max; j++){
                if (!inRow(j,a,i)){
                    System.out.println("Not in row");
                    return false;
                }
            }
        }
        return true;
    }
}
