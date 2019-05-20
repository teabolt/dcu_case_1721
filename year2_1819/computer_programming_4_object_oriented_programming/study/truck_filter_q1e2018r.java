import java.util.List;
import java.util.ArrayList;


class Truck {

    int engineSize;
    public Truck(int engineSize) {
        this.engineSize = engineSize;
    }
    public String toString() { return String.valueOf(engineSize); }

    public static List<Truck> smallEngine(List<Truck> trucks) {
        List<Truck> smallTrucks = new ArrayList<>();
        for (Truck truck : trucks) if (truck.engineSize < 2000) smallTrucks.add(truck);
        return smallTrucks;
    }
}


public class truck_filter_q1e2018r {

    public static void main(String[] args) {
        // Truck[] truckers = {new Truck(10000), new Truck(0)};
        List<Truck> truckers = new ArrayList<>();
        truckers.add(new Truck(10000));
        truckers.add(new Truck(100));
        truckers.add(new Truck(1999));
        truckers.add(new Truck(2000));
        truckers.add(new Truck(2001));
        List<Truck> smoolTruck = Truck.smallEngine(truckers);
        for (Truck truck : smoolTruck) System.out.println(truck);
    }
}