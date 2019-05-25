
import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;

public class PhoneNumbers
{
    public static void main(String [] args)
    {
        System.out.println("Enter a name and number, or a name and ? to query (!! to exit)");
        Scanner in = new Scanner(System.in);
        Map<String, String> phonebook = new HashMap<>();
        
        String command = in.nextLine();
        while (!command.equals("!!")) {
            String[] parts = command.split(" ");
            String name = parts[0];
            String request = parts[1];
            if (request.equals("?")) {
                if (phonebook.containsKey(name)) 
                    System.out.printf("%s has number %s\n", name, phonebook.get(name));
                else 
                    System.out.printf("Sorry, there is no %s\n", name);
            }
            else 
                phonebook.put(name, request);
            command = in.nextLine();
        }
        System.out.println("Bye");
    }
}