interface Shape {
    public double area();
}

class Rectangle implements Shape {
    double width;
    double height;

    public double area() {
        return width*height;
    }
}

public class shape_rectangle_q1f2018 {
    public static void main(String[] args) {
        Rectangle r = new Rectangle();
        System.out.println(r.area());
        r.width = 10;
        r.height = 5;
        System.out.println(r.area());
    }
}