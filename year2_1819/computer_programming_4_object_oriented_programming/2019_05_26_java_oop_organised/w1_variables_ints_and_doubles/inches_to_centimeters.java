
import java.util.Scanner;

public class Inches2cm
{
    public static void main(String [] args)
    {
        // Create a scanner object
        Scanner in = new Scanner(System.in);

        System.out.print("Please enter a quantity in inches: ");
        int inches = in.nextInt();
        
        // Find out how many inches (use a whole number for integers)
        final double inchToCm = 2.54;
        double result = inches * inchToCm;

        // Print out the result
        System.out.println(inches + " inch is " + result + " cm");
    }
}