
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Senti2
{
    
    public static boolean in_review(String word, String review_sentence) {
        for (int i = word.length(); i <= review_sentence.length(); i++) {
            if (word.equals(review_sentence.substring(i-word.length(), i))) {
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
            File movieReviewFile = new File(args[1]);
            Scanner movieReviewScanner = new Scanner(movieReviewFile);
            String word = args[0];
            
            int score;
            String review;
            int totalScore = 0;
            int numScore = 0;
            while (movieReviewScanner.hasNext()) {
                score = movieReviewScanner.nextInt(); // read the score as a way of skipping over it
                review = movieReviewScanner.nextLine();
                if (in_review(word, review)) {
                    totalScore += score;
                    numScore += 1;
                }
            }
            
            double averageScore = 0;
            if (numScore != 0) {
                averageScore = ((double) totalScore) / numScore;
            }
            System.out.printf("%s appears %d times.\n", word, numScore);
            System.out.printf("The average score of the reviews containing %s is %.2f\n", word, averageScore);
            movieReviewScanner.close();
        }
    }
}