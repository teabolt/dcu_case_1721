
public class Circle extends Shape
{
    private double radius;
    
    public Circle(String name, double radius) {
        super(name);
        this.radius = radius;
    }
    
    public double area() {
        return Math.PI * Math.pow(radius, 2);
    }

}