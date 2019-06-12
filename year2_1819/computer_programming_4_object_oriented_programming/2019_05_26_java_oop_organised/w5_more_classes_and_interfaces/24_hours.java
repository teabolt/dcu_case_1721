
public class Time
{
   // Private variables
   private int hour;
   private int minute;
   private String time;
   
   // Constructor (with a String parameter)
   public Time(String time) {
       this.time = time;
       hour = Integer.parseInt(time.substring(0, 2));
       minute = Integer.parseInt(time.substring(2));
   }
   
   // isLater(Time otherTime) // boolean method to compare two times
   public boolean isLater(Time otherTime) {
       if (this.hour > otherTime.hour) {
           return true;
       } else if (this.hour == otherTime.hour) {
           if (this.minute > otherTime.minute) {
               return true;
           }
       }
       return false;
   }
   
   // String toString() // return a String representation of the time (hh:mm)
   public String toString() {
       return time.substring(0, 2) + ":" + time.substring(2);
   }
}