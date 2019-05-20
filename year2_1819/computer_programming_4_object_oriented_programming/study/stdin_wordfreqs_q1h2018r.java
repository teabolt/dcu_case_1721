import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;


public class stdin_wordfreqs_q1h2018r {

    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        Map<String, Integer> wordFreqs = new HashMap<>();
        while (stdin.hasNext()) {
            String word = stdin.next();
            if (!wordFreqs.containsKey(word))
                wordFreqs.put(word, 1);
            else
                wordFreqs.put(word, wordFreqs.get(word)+1);
        }
        System.out.println(wordFreqs);
    }
}