
import java.util.Scanner;

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

    // Insert the isAfter method here.

    public boolean isOnOrAfter(Date other) {
        if (other.year <= this.year){
            if (other.month <= this.month){
                if (other.day <= this.day){
                    return true;
                }
            }
        }
        return false;
    }
    // Here is the main method which will read in a sequence of dates.
    // Modify it so that it prints the latest date.
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        String line;
        line = in.nextLine();
        Date max_date = new Date(line);
        while(in.hasNextLine())
        {
            line = in.nextLine();
            if (line.length() != 0) {
                Date date = new Date(line);
                // Do what you want with the date.
                if (date.isOnOrAfter(max_date)) {
                    max_date = date;
                }
            }
        }
        System.out.println(max_date); // Print the latest date
    }
}
