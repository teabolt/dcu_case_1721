
public class Point
{
   private double x;
   private double y;

   public Point(double newX, double newY)
   {
      x = newX;
      y = newY;
   }
   
   public Point midPoint(Point other){
       double mX = (this.x + other.x)/2.0;
       double mY = (this.y + other.y)/2.0;
       return new Point(mX, mY);
       
   }

   public String toString()
   {
      return "(" + x + ", " + y + ")";
   }
}