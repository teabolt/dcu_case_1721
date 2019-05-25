
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;

public class WriteStudents
{
   public static void main(String [] args)
   {
        if (args.length == 2) {
            Scanner in = null;
            PrintWriter out = null;
            try {
                // read students into array
                File inputFile = new File(args[0]);
                in = new Scanner(inputFile);
                int studentNum = in.nextInt();
                Student[] group = new Student[studentNum];
                String name;
                int mark;
                for (int i = 0; i < studentNum; i++) {
                    name = in.next();
                    mark = in.nextInt();
                    group[i] = new Student(name, mark);
                }
                
                // increase student marks
                for (Student stud : group) {
                    stud.mark += 1; // would use setter method if it was available
                }
                
                // write out students
                out = new PrintWriter(args[1]);
                out.println(studentNum);
                for (Student stud : group) {
                    out.println(stud.name + " " + stud.mark); // would use student's toString otherwise
                }
            } catch (FileNotFoundException e) {
                System.out.println(e);
            } finally {
                in.close();
                out.close();
            }
        } else {
            System.out.println("Command line arguments do not match");
        }
   }
}