
/*
    This code is supplied and may be used to solve this problem.
*/
import java.util.Scanner;

public class OnlyHigh
{
    public static void main(String [] args)
    {
        // Create a scanner object
        Scanner in = new Scanner(System.in);
        
        System.out.print("Enter a word: ");
        // Read in the word
        String word = in.next();
        
        String cut;

        for (int i = 0; i < word.length() - 1; i++)
        {
            cut = word.substring(i,i+2);
            if (cut.equals("hi"))
            {
                System.out.println("hi");
            }
        }
        
    }
}