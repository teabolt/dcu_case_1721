import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;

import java.util.Collections;
import java.util.List;
import java.util.ArrayList;


public class MakeMap {

    public static Map<String, Integer> makeMap(Scanner in) {
    	Map<String, Integer> map = new HashMap<String, Integer>();
    	while (in.hasNext()) {
    		String name = in.next();
    		int mark = in.nextInt();
    		map.put(name, mark);
    	}
    	return map;
    }

   	public static void main(String [] args) {
      Map<String, Integer> students = MakeMap.makeMap(new Scanner(System.in));

      List<String> names = new ArrayList<String>(students.keySet());
      Collections.sort(names);
      for(String name : names)
         System.out.println(name + " has mark " + students.get(name));
   	}

}