
//
// Supplied code to help ensure there will be no output formatting issues.
//
import java.util.Scanner;

public class AboveAverage
{
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        
        System.out.print("How many numbers: ");
        int num = in.nextInt();
        
        // Create an array
        double[] numbers;
        numbers = new double[num];
        double sum = 0;
        
        System.out.print("Enter " + num + " numbers: ");
        
        // Now read in the numbers
        for(int i = 0; i < num; i++)
        {
             double x = in.nextDouble();
             numbers[i] = x;
             sum += x;
        }

        double average = sum / num;
        // Print out the numbers greater than the average
        System.out.println("The above average numbers are:");
        for(int i = 0; i < num; i++) {
            // You can use the following code to print out one number
            if (average < numbers[i]) {
            System.out.print(" " + numbers[i]); // You may want to put this in a loop.
            }
        }

        System.out.println(); // Should finish with a new line
    }
}