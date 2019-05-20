abstract class Vehicle {
    public abstract void go();
}


class Porsche extends Vehicle {
    public void go() { System.out.println("vrrrmm"); }
}


class Banger extends Vehicle {
    public void go() { System.out.println("bangbang"); }
}


public class vehicle_abstract_q3a2018 {
    public static void main(String[] args) {
        Vehicle v1 = new Porsche();
        Vehicle v2 = new Banger();
        Vehicle[] cars = {v1, v2};
        for (Vehicle v : cars) v.go();
    }
}