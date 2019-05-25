
import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;

public class Previous
{
    public static void main(String [] args)
    {
        System.out.println("Enter some numbers (-1 to end)");
        Scanner in = new Scanner(System.in);
        Set<Integer> seen = new HashSet<>();
        
        System.out.println("Previous:");
        int num = in.nextInt();
        while (num != -1) {
            if (seen.contains(num)) {
                System.out.println(num);
            } else {
                seen.add(num);
            }
            num = in.nextInt();
        }
    }
}