
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class ReadNames
{
    public static void main(String [] args)
    {
        Scanner stdin = new Scanner(System.in);
        Scanner in = null; // set up for 'finally'
        System.out.print("Enter the file name: ");
        try {
            File file = new File(stdin.next());
            in = new Scanner(file);
            
            int numNames = in.nextInt();
            String[] names = new String[numNames];
            
            for (int i = 0; i < numNames; i++) {
                names[i] = in.next();
            }
            
            System.out.println("The names in reverse order are:");
            for (int i = names.length-1; 0 <= i; i--) {
                System.out.print(names[i] + " ");
            }
        } catch (FileNotFoundException e) {
            System.out.println(e);
        }
        finally {
            in.close();
        }
    }
}