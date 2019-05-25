
import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class ListSort
{
    public static void main(String [] args)
    {
        List<Integer> nums = new ArrayList<Integer>();
        
        System.out.print("Enter numbers: ");
        
        Scanner in = new Scanner(System.in);
        
        int num = in.nextInt();
        while(num != -1)
        {
            nums.add(num);
            num = in.nextInt();

        }
        Collections.sort(nums);
        System.out.print("Sorted: ");
        for(int number : nums)
            System.out.print(number +" ");

    }
}