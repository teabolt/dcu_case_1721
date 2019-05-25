
import java.util.Scanner;

public class OneToNum
{
    public static void main(String [] args)
	{
		Scanner reader = new Scanner(System.in);
		int i = 1;
		int n = reader.nextInt();
		while (i <= n)
		{
			System.out.print(i+" ");
			i++;
		}
	    System.out.println();
	}
}