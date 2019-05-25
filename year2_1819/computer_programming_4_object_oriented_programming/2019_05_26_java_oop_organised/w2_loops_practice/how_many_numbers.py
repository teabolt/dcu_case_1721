
import java.util.Scanner;

public class HowManyNumbers
{
    public static void main(String [] args)
	{
	    System.out.print("Enter numbers: ");
	   	Scanner input = new Scanner(System.in);
	   	System.out.println();
	    int total = 0;
	    int n = input.nextInt();
	    while (n != -1) {
	        total += 1;
	        n = input.nextInt();
	    }
	    System.out.printf("%d numbers were entered.\n", total);
	}
}