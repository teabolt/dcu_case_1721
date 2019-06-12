
public class Date
{
    private int day;
    private int month;
    private int year;

    public Date(String input){
        String[] parts = input.split(" ");
        this.day = Integer.parseInt(parts[0]);	
        this.month = Integer.parseInt(parts[1]);
        this.year = Integer.parseInt(parts[2]);
    }
    
    public String toString()
    {
        return day + "/" + month + "/" + year;
    }
    
    // Create a boolean method which will check to sae that the date is on or after the date that is passed as a parameter.
    public boolean isOnOrAfter(Date other) {
        if (other.year < this.year) return true;     
        else if (other.month < this.month) return true;
        else if (other.day < this.day) return true;
        return other.year == this.year && other.month == this.month && other.day == this.day;
    }
}

