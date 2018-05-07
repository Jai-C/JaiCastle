
/**
 * A TextAnalyser object takes text (either directly as a String, or read in from a file), 
 * and it maintains a count of the occurrences of each letter in that text. 
 * 
 * So e.g. analysing the text "A tap tot" would mean adding 
 * 1 each to the counts for O and P, 
 * 2 to the count for A, and 
 * 3 to the count for T. 
 * 
 * Letters are regarded as case-insensitive (so e.g. count bs and Bs together). 
 * Non-letter characters are ignored. 
 * The counts for each text analysed are added together until a reset operation is invoked. 
 * The class provides various methods for interrogating the data. 
 * 
 * @author Jai Castle (modified from Lyndon While)
 * @version 1.1 
 */
import java.util.Arrays;

public class TextAnalyser
{
    private int   letters;     // the total number of letters analysed since the last reset 
    private int[] frequencies; // the number of occurrences of each letter of the alphabet (case-insensitive) 

    // initialise the two instance variables 
    public TextAnalyser()
    {
        letters = 0;
        frequencies = new int[26];
    }
    
    // initialise the two instance variables, and analyse the String initial 
    public TextAnalyser(String initial)
    {
        letters = 0;
        frequencies = new int[26];
        analyse(initial);
        System.out.println(Arrays.toString(frequencies));
    }
    
    // analyse the String s 
    // add to each count in frequencies the number of occurrences of each letter in s, and update letters 
    // remember that non-letter characeters must be ignored
    public void analyse (String s)
    {
        s = s.toLowerCase();
        for (int i = 0; i < s.length(); i++){
            char character = s.charAt(i);
            if ((int) character <= 122 && (int) character >= 97){
                frequencies[character - 97] = frequencies[character - 97] + 1;
                letters++;
            }
        }
    }
    
    // analyse the contents of the file f 
    // read in the file as a FileIO object, then analyse the contents 
    public void analyseFile (String f)
    {
        FileIO file = new FileIO(f);
        for (String line: file.lines){
            analyse(line);
        }
        System.out.println(Arrays.toString(frequencies));
    }

    // clear the instance variables 
    public void reset() 
    {
        frequencies = new int[26];
        letters = 0;
    }
    
    // return the number of letters that have been seen since the last reset 
    public int lettersAnalysed()
    {
        return letters;
    }
    
    // return the number of occurrences of letter that have been seen since the last reset 
    public int frequency (char letter)
    {
        if (letter >= 'a' && letter <= 'z'){
            return frequencies[(int) letter - 97];
        }
        else return 0;
    } 
    
    // return the most common letter seen since the last reset 
    // if no letters have been analysed, return '?' 
    public char mostFrequent()
    {
        int maxIndex = 0;
        int maximum = frequencies[maxIndex];
        for (int index = 0; index < frequencies.length; index++){
            if (frequencies[index] > maximum){
                maxIndex = index;
                maximum = frequencies[index];
            }
        }
        if (maximum != 0) return (char) (maxIndex + 97);
        else return '?';
    }
    
    // use Oblongs to draw a histogram of the frequencies 
    // create an Oblong for each bar of the histogram, and arrange them appropriately on the screen 
    public void histogram()
    {
        int s = 10;
        for (int k = 0; k < 26; k++)
            new Oblong(0, 5 + k * (s + 1), frequency((char) ('a' + k)), s, "red");
    }

}
