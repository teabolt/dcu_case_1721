import java.util.Scanner;
import java.util.Map;
// import java.util.HashMap;
import java.util.TreeMap;

public class WordLength {

	static Map<Integer, Integer> mapLength(Scanner in) {
		Map<Integer, Integer> lengths = new TreeMap<>(); // keys are ordered
		while (in.hasNext()) {
			String word = in.next();
			int len = word.length();
			
			Object currentValue = lengths.putIfAbsent(len, 1);
			if (currentValue != null) {
				lengths.put(len, ((int) currentValue)+1);
			}
			// OR
			// if (!lengths.containsKey(len)) {
			// 	lengths.put(len, 1);
			// } else {
			// 	lengths.put(len, lengths.get(len)+1);
			// }
		}
		return lengths;
	}

    public static void main(String [] args) {
    	Scanner in = new Scanner(System.in);
    	Map<Integer, Integer> lengths = mapLength(in);
    	lengths.forEach((k, v) -> {System.out.printf("%d: %d\n", k, v);}); // use a lambda (BiConsumer)
    }
}