
import java.util.Scanner;

public class IsTeenager
{
    // Fill in the main method
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter your age: ");
        int age = in.nextInt();
        
        if ((age < 20) && (age > 12)) {
            System.out.println("You are a teenager.");
        }
        else {
            System.out.println("You are not a teenager.");
        }
    }
}