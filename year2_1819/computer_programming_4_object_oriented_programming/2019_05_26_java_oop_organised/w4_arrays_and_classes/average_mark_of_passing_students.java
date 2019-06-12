
public class Test
{
   public static double getPassingAverage(Student [] student)
   {
      double total = 0;
      double marks = 0;
      for(int i = 0; i < student.length; i++)
      { if (student[i].getMark() >= 40)
        {    
            total += 1;
            marks += student[i].getMark();
        }
      }
      if (total != 0)
        return marks/total;
      return 0;
   }
}