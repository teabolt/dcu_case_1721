import java.util.Map;
import java.util.TreeMap;
import java.util.HashMap;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;


class MakeMap {

    public static Map<String, Integer> makeMap(Scanner reader) {
        Map<String, Integer> myMap = new HashMap<>();
        while (reader.hasNext()) {
            String token = reader.next();
            int integral = reader.nextInt();
            myMap.put(token, integral);
        }
        return myMap;
    }
}


public class makemap_scanner_q1h2018 {

    public static void main(String[] args) throws FileNotFoundException {
        Scanner sc = new Scanner(new File(args[0]));
        Map<String, Integer> mapper = MakeMap.makeMap(sc);
        System.out.println(mapper);
    }
}