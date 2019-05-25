
import java.util.Scanner;
public class StringReproduction {
	public static void main(String [] args)
	{
		Scanner input = new Scanner(System.in);
		
		System.out.print("Enter an integer and a string: ");
		
		int n = input.nextInt();
		String s = input.next();
		
		for(int i = 0; i < n; i++)
		{
			System.out.print(s);
		}
		
		System.out.println();
		
		
	}
}
