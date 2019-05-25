
import java.util.Scanner;

public class NoMinusOne {
	public static void main(String [] args)
	{
		System.out.print("Enter numbers: \n");
		Scanner input = new Scanner(System.in);
		int n;
		int penultimate = -1;
		do
		{
			n = input.nextInt();
			if (n != -1)
			{
				penultimate = n;
			}
		}
		while(n != -1);
		
		if (penultimate != -1 )
		{
		System.out.printf("The penultimate number was: %d\n",penultimate);
		}
	}
}
