class Vehicle {

    private int numWheels;
    private int numDoors;

    public Vehicle(int wheels, int doors) {
        setWheels(wheels);
        setDoors(doors);
    }

    public Vehicle() { 
        setWheels(4);
        setDoors(4);
    }

    public int getWheels() { return numWheels; }
    public void setWheels(int wheels) { numWheels = wheels; }

    public int getDoors() { return numDoors; }
    public void setDoors(int doors) { numDoors = doors; }

    public String toString() {
        return String.format("Vehicle: %d wheelers, %d exits", getWheels(), getDoors());
    }
}


public class vehicle_q1d2018r {

    public static void main(String[] args) {
        Vehicle v1 = new Vehicle(-1, 43);
        Vehicle v2 = new Vehicle();
        System.out.println(v1);
        System.out.println(v2);
        v2.setDoors(5);
        System.out.println(v2);
    }
}