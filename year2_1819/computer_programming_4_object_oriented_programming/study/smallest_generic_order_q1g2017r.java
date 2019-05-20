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


class GenericOps {

    public static <T extends Order> T smallest(T leftItem, T rightItem) {
        if (rightItem.lessThan(leftItem)) return rightItem;
        else return leftItem;
    }
}


public class smallest_generic_order_q1g2017r {

    public static void main(String[] args) {
        Point p1 = new Point(3, 5);
        Point p2 = new Point(3, 4);
        System.out.println(GenericOps.smallest(p1, p2));
    }
}