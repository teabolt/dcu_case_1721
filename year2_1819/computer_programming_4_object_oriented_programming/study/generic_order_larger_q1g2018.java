public class generic_order_larger_q1g2018 {

    public static <T extends Order> T larger(T leftItem, T rightItem) {
        if (leftItem.lessThan(rightItem)) return rightItem;
        else return leftItem;
    }

    public static void main(String[] args) {
        Star s1 = new Star(100000000);
        Star s2 = new Star(100000);
        System.out.println(larger(s1, s2));
    }
}

class Star implements Order {
    int brightness;

    public Star(int brightness) { this.brightness = brightness; }

    public String toString() { return String.valueOf(brightness); }

    public boolean lessThan(Order other) {
        Star otherStar = (Star) other;
        return brightness < otherStar.brightness;
    }
}

interface Order {
    public boolean lessThan(Order other);
}