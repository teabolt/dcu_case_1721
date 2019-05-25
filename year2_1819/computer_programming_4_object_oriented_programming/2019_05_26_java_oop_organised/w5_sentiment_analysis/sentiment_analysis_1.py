
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Senti1
{
    public static int occurs(String w, String[] s) {
        int occurrences = 0;
        for (String token : s) {
            if (w.equals(token)) {
                occurrences += 1;
            }
        }
        return occurrences;
    }
    
    public static int sub_occurs(String w, String s) {
        int occurrences = 0;
        for (int i = w.length(); i <= s.length(); i++) {
            if (w.equals(s.substring(i-w.length(), i))) {
                occurrences += 1;
            }
        }
        return occurrences;

    }
    
    public static void main(String [] args) throws FileNotFoundException
    {
        if (args.length != 2) {
            System.out.println("An incorrect number of command line arguments was supplied.");
        } else {
            File movieReviewFile = new File(args[1]);
            Scanner movieReviewScanner = new Scanner(movieReviewFile);
            String word = args[0];
            
            int score;
            String review;
            int total_occurrences = 0;
            while (movieReviewScanner.hasNext()) {
                score = movieReviewScanner.nextInt(); // read the score as a way of skipping over it
                review = movieReviewScanner.nextLine();
                String[] review_words = review.split(" ");
                // total_occurrences += Senti1.occurs(word, review_words);
                total_occurrences += Senti1.sub_occurs(word, review);
            }
            
            System.out.printf("%s appears %d times.\n", word, total_occurrences);
            movieReviewScanner.close();
        }
    }
}