/**
* (Deprecated) Some tests for helper classes.
**/
public class Tests {

    static void test_matrix() {
        Matrix m = new Matrix(3, 2);
        System.out.println(m.get(0, 0));
        m.put(0, 0, 1);
        m.put(0, 1, 2);
        m.put(1, 0, 3);
        m.put(1, 1, 4);
        System.out.println(m.get(0, 0));
        System.out.println();
        System.out.println(m);
        // TODO: invalid values
    }

    public static void main(String[] args) {
        System.out.println("testing matrix implementation");
        test_matrix();
    }
}