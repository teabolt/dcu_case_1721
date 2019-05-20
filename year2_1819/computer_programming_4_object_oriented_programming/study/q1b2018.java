import java.util.Set;
import java.util.HashSet;

public class q1b2018 {

    // public static boolean allDoneSet(String word, String guessed) {
    //     Set<Character> wordSet = new HashSet<Character>(word);
    //     // wordSet.addAll(word);
    //     System.out.println(wordSet);
    //     return true;
    // }

    public static boolean allDone(String word, String guessed) {
        for (int i = 0; i < word.length(); i++) {
            String wordCh = word.substring(i, i+1);
            if (!guessed.contains(wordCh)) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(allDone("computer", "putxmocre"));
        System.out.println(allDone("computer", "xcomp"));
        System.out.println(allDone("", ""));
        System.out.println(allDone("aha", "ah"));
        System.out.println(allDone("baba", "raleb"));
        System.out.println(allDone("", "raleb"));
    }
}