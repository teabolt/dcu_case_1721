
// Make the Date class implement the comparable interface
public class Date implements Comparable<Date>
{
   private int day, month, year;

   public Date(int day, int month, int year)
   {
      this.day = day;
      this.month = month;
      this.year = year;
   }
   public int compareTo(Date other)
   {
       if(this.year < other.year)
       {
           return -1;
       }
       else if(this.year > other.year)
       {
           return +1;
       }
       else
       {
           if(this.month < other.month)
           {
               return -1;
           }
           else if (this.month > other.month)
           {
            return +1;               
           }
           else
           {
               if(this.day < other.day)
               {
                return -1;
               }
               else if(this.day > other.day){
                   return +1;
               }else{return 0;}
           }
       }
           
   }
   public String toString()
   {
      return day + "/" + month + "/" + year;
   }
}

