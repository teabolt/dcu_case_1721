
import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;
import java.io.FileNotFoundException;
import java.io.File;

public class Suspicious
{
    public static void main(String [] args)
    {
        try {
            Scanner studFile = new Scanner(new File(args[0]));
            Set<String> students = new HashSet<>();
            while (studFile.hasNext()) 
            {
                String student = studFile.nextLine();
                students.add(student);
            }
            studFile.close();
            
            Scanner deliFile = new Scanner(new File(args[1]));
            int counter = 1;
            while (deliFile.hasNext()) 
            {
                String delinquent = deliFile.nextLine();
                if (students.contains(delinquent)) {
                    System.out.printf("%d. %s\n", counter, delinquent);
                    counter++;    
                }
            }
            deliFile.close();
        } catch (FileNotFoundException e) {
            System.out.println(e);
        }
    }
}