
public class Point implements Order
{
    private double x, y;
    
    public Point(double newX, double newY)
    {
        x = newX;
        y = newY;
    }
    
    public String toString()
    {
        return "(" + x + ", " + y + ")";
    }

    public static double pos(double num){
        if (num < 0) 
            return num*-1;
        return num;
    }    

    public boolean lessThan(Order other) {
        // Point Minp = (Point) other;
        // if((pos(this.x) + pos(this.y)) > (pos(Minp.x) + pos(Minp.y))){return false;}
        // return true;
        Point otherPoint = (Point) other;
        return (Math.pow(this.x, 2) + Math.pow(this.y, 2)) < (Math.pow(otherPoint.x, 2) + Math.pow(otherPoint.y, 2));
        }
}