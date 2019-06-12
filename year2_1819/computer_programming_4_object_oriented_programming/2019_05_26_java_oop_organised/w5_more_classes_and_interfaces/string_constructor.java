
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
}