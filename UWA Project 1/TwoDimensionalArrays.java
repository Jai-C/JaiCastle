/**
 * 2D dimensional arrays calculations
 *
 * @author Jai Castle
 * @version 30 April 2018
 */
public class TwoDimensionalArrays
{
    // returns the largest element in a 2d array
    // e.g. max({{1, 3}, {7, -2, 0}, {4, 4}}) = 7
    public static int max(int[][] a)
    {
        int maximum = a[0][0];
        
        for (int[] array: a){
            for (int element: array){
                if (element > maximum){
                    maximum = element;
                }
            }
        }
        return maximum;
    }

    // returns the sum of the elements in the xth row in a 
    // e.g. rowSum({{3}, {8, -2, 6}, {5, -2}}, 1) = 8 + (-2) + 6 = 12
    public static int rowSum(int[][] a, int x)
    {
        int sum = 0;
        for (int element: a[x]){
            sum += element;
        }
        return sum;
    }

    // returns the sum of the elements in the xth column in a
    // e.g. columnSum({{3, 4}, {6}, {0, 8, -2}}, 1) = 4 + 8 = 12 
    public static int columnSum(int[][] a, int x)
    {
        int sum = 0;
        for (int[] array: a){
            if (x < array.length){
                sum += array[x];
            }
        }
        return sum;
    }

    // returns an array holding the sums of the rows in a 
    // e.g. allRowSums({{1}, {2, 3}, {4, 5, 6}}) = {1, 5, 15}
    public static int[] allRowSums(int[][] a)
    {
        int[] sums = new int[a.length];
        int i = 0;
        for (int[] array: a) {
            int rowSum = 0;
            for (int element: array){
                rowSum += element;
            }
            sums[i] = rowSum;
            i++;
        }
        return sums;
    }

    // returns true iff a is square, 
    // i.e. iff every row has the same length as the number of rows 
    public static boolean isSquare(int[][] a)
    {
        int height = a.length;
        for (int[] array: a){
            if (array.length != height){
                return false;
            }
        }
        return true;
    }

}
