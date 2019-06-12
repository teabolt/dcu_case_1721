
public class Animal
{
    private String name;
    
    public Animal(String name)
    {
        this.name = name;
    }
    
    public String getName() {return this.name;}
    
    public String greeting()
    {
        return String.format("Hello, my name is %s", getName());
    }
}