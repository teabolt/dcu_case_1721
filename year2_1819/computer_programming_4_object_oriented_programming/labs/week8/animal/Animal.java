public class Animal {

    String name;

    public Animal(String name) {
        this.name = name;
    }

    public String greeting() {
        return String.format("Hello, my name is %s", name);
    }
}