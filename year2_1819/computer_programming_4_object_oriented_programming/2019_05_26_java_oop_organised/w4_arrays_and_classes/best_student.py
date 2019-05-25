
public class Test
{
    // Add a static getBestSTudent method to this class. It should return a Student object.

   public static Student getBestStudent(Student [] student)
   {
      Student best_student = student[0];
      for(int i = 1; i < student.length; i++)
      { if (student[i].getMark() > best_student.getMark())
            best_student = student[i];
      }
      return best_student;
   }    
}