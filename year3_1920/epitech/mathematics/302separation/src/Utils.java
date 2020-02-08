import java.util.List;


/**
* Utility functions.
**/
public class Utils {

    public static <T> void printArray(T[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + ",");
        }
        System.out.println();
    }

    public static int[] integerListToArray(List<Integer> lst) {
        int arr[] = new int[lst.size()];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = lst.get(i);
        }
        return arr;
    }
}