
import java.util.Scanner;

public class OneToNum
{
    public static void main(String [] askjda)
    {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a number: ");
        
        int n = input.nextInt();
        
        for(int i = 1 ; i <= n ; i++)
        {
            System.out.print(i + " ");
        }
        
        System.out.println();
    }
}