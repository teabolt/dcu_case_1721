
public class Pair<U, V> {
    private U thing1;
    private V thing2;
    
    public Pair(U thing1, V thing2) {
        this.thing1 = thing1;
        this.thing2 = thing2;
    }
    
    public String toString() {
        return thing1.toString() + " " + thing2.toString();
    }
}