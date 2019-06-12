
import java.util.Scanner;

public class DoubleDivision
{
    // Fill in the main method
    public static void main(String [] args) {

        Scanner in = new Scanner(System.in);

        System.out.print("Please enter two floating point numbers: ");
        double num = in.nextDouble();
        double num2 = in.nextDouble();

        double result = num / num2;

        System.out.println(num + " / " + num2 + " is " + result);
    }
}