
import java.util.Scanner;

public class TwoTimes {
	public static void main(String [] args)
	{
		System.out.print("Enter a number: ");
		Scanner input = new Scanner(System.in);
		int n = input.nextInt();
		System.out.printf("Times two is: %d\n",Helper.twoTimes(n));
		
		
	}
}
