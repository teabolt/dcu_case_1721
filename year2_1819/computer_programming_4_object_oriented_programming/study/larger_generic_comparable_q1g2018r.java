interface Comparable<T> {
    int compareTo(T other);
}


class Truck implements Comparable<Truck> {

    int engineSize;
    public Truck(int engineSize) {
        this.engineSize = engineSize;
    }
    public String toString() { return String.valueOf(engineSize); }

    @Override
    public int compareTo(Truck other) {
        if (engineSize < other.engineSize) return -1;
        else if (other.engineSize < engineSize) return 1;
        else return 0;
    }
}


class GenericOperators {

    public static <T extends Comparable<T>> T larger(T leftItem, T rightItem) {
        // can leave out the <? super T> part, but will get a compiler warning
        int ordering = leftItem.compareTo(rightItem);
        if (ordering == 1) return leftItem; // leftItem is greater
        else return rightItem;  // rightItem is greater or the items are equal
    }
}


public class larger_generic_comparable_q1g2018r {

    public static void main(String[] args) {
        Truck t1 = new Truck(1000);
        Truck t2 = new Truck(2000);
        System.out.println(GenericOperators.larger(t2, t1));
    }
}