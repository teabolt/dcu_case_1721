
public class Test
{
    // Add a static getBestSTudent method to this class. It should return a Student object.

   public static int numberPasses(Student [] student)
   {
      int total = 0;
      for(int i = 0; i < student.length; i++)
      { if (student[i].getMark() >= 40)
            total += 1;
      }
      return total;
   }    
}