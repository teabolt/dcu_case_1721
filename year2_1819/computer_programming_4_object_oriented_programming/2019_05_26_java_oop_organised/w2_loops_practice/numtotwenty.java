
import java.util.Scanner;

public class NumToTwenty
{
    public static void main(String [] args)
	{
		Scanner reader = new Scanner(System.in);
		System.out.print("Enter a number: ");
		int i = reader.nextInt();
		while (i <= 20)
		{
			System.out.print(i+" ");
			i++;
		}
	    System.out.println();
	}
}