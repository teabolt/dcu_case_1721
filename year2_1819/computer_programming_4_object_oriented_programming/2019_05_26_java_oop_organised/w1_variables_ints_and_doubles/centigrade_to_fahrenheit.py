
import java.util.Scanner;

public class Cent2Fahr
{
    public static void main(String [] args)
    {
        // Create a scanner object
        Scanner in = new Scanner(System.in);

        int celsius = in.nextInt();
        double fahrenheit = (celsius * 1.8) + 32;
        System.out.println(celsius + " " + fahrenheit);

   }
}