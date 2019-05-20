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


public class truck_comparable_q1f2018r {

    public static void main(String[] args) {
        Truck t1 = new Truck(1000);
        Truck t2 = new Truck(2000);
        System.out.println(t1.compareTo(t2)); // -1
        System.out.println(t2.compareTo(t2)); // 0
        System.out.println(t2.compareTo(t1)); // 1
    }
}