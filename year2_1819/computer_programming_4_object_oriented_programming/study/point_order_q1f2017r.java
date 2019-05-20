class Point implements Order {
    private double x, y;

    public Point(double newX, double newY) {
        x = newX;
        y = newY;
    }

    public String toString() {
        return "(" + x + ", " + y + ")";
    }

    @Override
    public boolean lessThan(Order other) {
        Point otherPoint = (Point) other;
        if (x < otherPoint.x) return true;
        else if (otherPoint.x < x) return false;
        else {
            if (y < otherPoint.y) return true;
            else return false; // greater or equal
        }
    }
}


interface Order {
    public boolean lessThan(Order other);
}


public class point_order_q1f2017r {

    public static void main(String[] args) {
        Point p1 = new Point(2, 3);
        Point p2 = new Point(3, 4);
        Point p3 = new Point(2, 5);
        Point p4 = new Point(2, 2);
        System.out.println(p1.lessThan(p2)); // true
        System.out.println(p1.lessThan(p3)); // true
        System.out.println(p1.lessThan(p4)); // false
    }
}