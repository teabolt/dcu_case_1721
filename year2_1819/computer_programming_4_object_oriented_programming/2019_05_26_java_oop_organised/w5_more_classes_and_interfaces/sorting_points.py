
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
    
    public boolean lessThan(Order other) {
        Point otherPoint = (Point) other;
        return (Math.pow(this.x, 2) + Math.pow(this.y, 2)) < 
        (Math.pow(otherPoint.x, 2) + Math.pow(otherPoint.y, 2));
    }
    
}