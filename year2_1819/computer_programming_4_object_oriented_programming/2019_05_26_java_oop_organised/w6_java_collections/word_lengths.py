
import java.util.Scanner;
import java.util.Map;
import java.util.TreeMap;

public class WordLength
{
    public static void main(String [] args)
    {
        Map<Integer, Integer> wordLengths = new TreeMap<>();
        Scanner in = new Scanner(System.in);

        while(in.hasNext())
        {
            String word = in.next();
            int len = word.length();
            if(wordLengths.containsKey(len))
                wordLengths.put(len, wordLengths.get(len)+1);
            else
                wordLengths.put(len, 1);         
        }
        wordLengths.forEach((k,v) -> {System.out.printf("%d: %d\n", k, v);});
    }
}