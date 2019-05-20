import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class GroupStudents
{
   public static void main(String [] args)
   {
    // Scanner stdin = new Scanner(System.in);
    // String filename = stdin.next();
    if (0 < args.length) {
        Scanner in = null;
        try {
            File file = new File(args[0]);
            in = new Scanner(file);
            int studentNum = in.nextInt();
            Student[] group = new Student[studentNum];
            
            String name;
            int mark;
            for (int i = 0; i < studentNum; i++) {
                name = in.next();
                mark = in.nextInt();
                group[i] = new Student(name, mark);
            }

            Student.print(group);
        } catch (FileNotFoundException e) {
            System.out.println(e);
        } finally {
            in.close();
        }
    }
   }
}