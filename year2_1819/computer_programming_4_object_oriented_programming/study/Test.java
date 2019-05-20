import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class Test {

    public static void main(String[] args) {
        System.out.println(
            String.format("This is a integer: %d, a string: %s, and a float: %f", 10, "aha", -3.5)
        );
    }
}


class MyType {

    public static void saySomething() {
        System.out.println("ello");
    }
}


class MySubtype extends MyType {

    public static void sayNothing() {
        System.out.println("nothing");
    }
}

interface SomeInterface {}
interface SomeOtherInterface{}

class SomeClass {}
class SomeOtherClass {}

class SomeType {}
class SomeOtherType{}

class Generic 
<T extends SomeType & SomeOtherInterface, 
V extends SomeOtherType & SomeInterface & SomeOtherInterface,
W> 
    extends SomeClass 
    implements SomeInterface, SomeOtherInterface {}