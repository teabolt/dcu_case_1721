
import java.util.Scanner;

public class EvenOdd
{
    // Fill in the main method
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = in.nextInt();
        
        if (num % 2 == 0) {
            System.out.println(num + " is even.");
        }
        else {
            System.out.println(num + " is odd.");
        }
    }
}