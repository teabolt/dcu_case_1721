
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
    
    public boolean lessThan(Order other){
        
        // Point Minp = (Point) other;
        // //if (this.x >= Minp.x){
        // //    if(this.y >= Minp.y){
        // //        return false;
        // //    }
        // //}
        // //return true;
        // //if (Minp.x < this.x){return false;}
        // //if (Minp.y < this.x){return false;}
        // //return true;
        
        // if (Minp.x < this.x){
        //     return false;
        // } else if (Minp.x > this.x){
        //     return true;
        // }
        
        // if (Minp.y < this.y){
        //     return false;
        // } else if (Minp.y > this.y){
        //     return true;
        // }
        // return true;
        
        // this < other
        Point otherPoint = (Point) other;
        return (this.x < otherPoint.x) || (this.x == otherPoint.x && this.y < otherPoint.y);
    }
}