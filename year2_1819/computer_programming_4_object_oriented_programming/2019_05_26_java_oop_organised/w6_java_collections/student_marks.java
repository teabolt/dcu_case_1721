
import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;

public class MakeMap {

    public static Map<String, Integer> makeMap(Scanner in) {
    	Map<String, Integer> map = new HashMap<>();
    	while (in.hasNext()) {
    		String name = in.next();
    		int mark = in.nextInt();
    		map.put(name, mark);
    	}
    	return map;
    }
}