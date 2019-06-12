
import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

public class EvenOdd
{
    public static void main(String [] args)
    {
        List<Integer> odds = new ArrayList<Integer>();
        List<Integer> evens = new ArrayList<Integer>();
        System.out.print("Enter numbers: ");
        
        Scanner in = new Scanner(System.in);
        
        int num = in.nextInt();
        while(num != -1)
        {
            if(num % 2 == 0)
                evens.add(num);
            else
                odds.add(num);
            num = in.nextInt();
        }
        System.out.print("Odd: ");
        for(int n_odd : odds)
            System.out.print(n_odd + " ");
        System.out.println();
        System.out.print("Even: ");
        for(int n_even : evens)
            System.out.print(n_even + " ");
        System.out.println();
    }
}