import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;


public class read_occurrences_q2c {

    public static Map<String, Integer> generateFrequencyMapping(Scanner sc) {
        Map<String, Integer> wordFreqs = new HashMap<>();

        while (sc.hasNext()) {
            String token = sc.next();
            String[] words = token.split("\\.");

            for (String word : words) {
                System.out.println(word);
                if (!wordFreqs.containsKey(word))
                    wordFreqs.put(word, 1);
                else
                    wordFreqs.put(word, wordFreqs.get(word)+1);
            }
        }
        return wordFreqs;
    }

    public static int countValue(Map<String, Integer> map, int value) {
        int count = 0;
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            String k = entry.getKey();
            int v = entry.getValue();
            if (v == value) count += 1;
        }

        // wordFreqs.forEach((word, occurrences) -> {
        //     if (occurrences == 1)
        //         System.out.println(word);
        // });

        return count;
    }

    public static void main(String[] args) throws IndexOutOfBoundsException, FileNotFoundException {
        String filename = args[0];
        File file = new File(filename);
        Scanner reader = new Scanner(file);
        Map<String, Integer> wordFreqs = generateFrequencyMapping(reader);

        int unique = countValue(wordFreqs, 1);
        System.out.println(unique);

        int twice = countValue(wordFreqs, 2);
        System.out.println(twice);
    } 
}