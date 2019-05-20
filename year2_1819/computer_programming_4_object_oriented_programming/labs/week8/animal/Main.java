import java.util.Scanner;

public class Main
{
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        
        String name = in.nextLine();
        
        Animal ani = new Animal(name);
        System.out.println(ani.greeting());
    }
}
