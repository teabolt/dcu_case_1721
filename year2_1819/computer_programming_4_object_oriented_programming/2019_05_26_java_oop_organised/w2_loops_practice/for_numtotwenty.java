
import java.util.Scanner;

public class NumToTwenty
{
    public static void main(String [] askjda)
    {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a number: ");
        
        for(int n = input.nextInt(); n <= 20 ; n++)
        {
            System.out.print(n + " ");
        }
        
        System.out.println();
    }
}