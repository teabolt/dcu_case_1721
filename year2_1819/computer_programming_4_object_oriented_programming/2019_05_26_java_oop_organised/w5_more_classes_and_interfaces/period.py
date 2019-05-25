
public class Period
{
   // Private variables
   // Constructor (with two Time parameters)
   // overlaps(Period otherPeriod) // boolean method to check if two periods overlap
   // String toString() // return a String representation of the Period
   
    private Time start;
    private Time end;

    public Period(Time start, Time end) {
       this.start = start;
       this.end = end;
    }
       
    public boolean overlaps(Period otherPeriod){
        return (otherPeriod.end.isLater(this.start) && this.end.isLater(otherPeriod.start)) 
        || (this.end.isLater(otherPeriod.start) && otherPeriod.end.isLater(this.start));
    }
    
    public String toString(){
        return (this.start.toString() + " -> " + this.end.toString());
    }
}