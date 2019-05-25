
/*
    This code is supplied and may be used to solve this problem.
*/
import java.util.Scanner;

public class ReducedString
{
    public static void main(String [] args)
    {
        // Create a scanner object
        Scanner in = new Scanner(System.in);
        
        System.out.print("Enter an integer and a string: ");
        // Read in the string
        int position = in.nextInt();
        String word = in.next();

        // work out what to print
        // YOUR CODE HERE
        System.out.println(word.substring(0, position) + word.substring(position + 1));
    }
}