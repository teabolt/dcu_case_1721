
import java.util.Scanner;

public class Reverse
{
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        
        // Read in the numbers
        System.out.print("How many numbers: ");
        int num = in.nextInt();
        
        System.out.print("Enter " + num + " numbers: ");
        int[] numbers = new int[num];
        for(int i = 0; i < num; i++)
        {
            numbers[i] = in.nextInt();
        }
        
        // reverse the numbers
        System.out.print("The numbers reversed are:");
        for(int i = numbers.length-1; i >= 0; i--) {
            System.out.print(" " + numbers[i]);
        }
        System.out.println();
    }
}