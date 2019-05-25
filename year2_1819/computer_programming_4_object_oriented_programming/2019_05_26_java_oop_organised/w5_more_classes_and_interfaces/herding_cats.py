
// Modify this class so that it implements the Order interface
public class Cat implements Order
{
    private String name;
    
    public Cat(String n)
    {
        name = n;
    }
    
    public String toString()
    {
        return "Cat: " + name;
    }
    
    public boolean lessThan(Order other) {
        // this < other
        Cat otherCat = (Cat) other;
        return this.name.length() < otherCat.name.length();
    }
}