
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Senti3
{
    public static boolean in_review(String word, String review_sentence) {
        for (int i = word.length(); i <= review_sentence.length(); i++) {
            if (word.equals(review_sentence.substring(i-word.length(), i))) {
                return true;
            }
        }
        return false;
    }
    
    public static int occurs(String w, String[] s) {
        int occurrences = 0;
        for (String token : s) {
            if (w.equals(token)) {
                occurrences += 1;
            }
        }
        return occurrences;
    }
    
    public static boolean occurs_full_in(String w, String[] s) {
        for (String token : s) {
            if (w.equals(token)) {
                return true;
            }
        }
        return false;
    }


    public static void main(String [] args) throws FileNotFoundException
    {
        if (args.length != 2) {
            System.out.println("An incorrect number of command line arguments was supplied.");
        } else {
            File wordFile = new File(args[0]);
            Scanner wordScanner = new Scanner(wordFile);
            File movieReviewFile = new File(args[1]);
            Scanner movieReviewScanner;

            while (wordScanner.hasNext()) {
                String word = wordScanner.next();
                int score;
                String[] review;
                int totalScore = 0;
                int numScore = 0;
                movieReviewScanner = new Scanner(movieReviewFile);
                while (movieReviewScanner.hasNext()) {
                    score = movieReviewScanner.nextInt();
                    review = movieReviewScanner.nextLine().split(" ");
                    if (occurs_full_in(word, review)) {
                        totalScore += score;
                        numScore += 1;
                    }
                }
                movieReviewScanner.close();
                double averageScore = 0;
                if (numScore != 0) {
                    averageScore = ((double) totalScore) / numScore;
                }
                System.out.printf("The score of %s is %.2f.\n", word, averageScore);
            }
            wordScanner.close();
        }
    }
}