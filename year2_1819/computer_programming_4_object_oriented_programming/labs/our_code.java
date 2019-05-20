import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Sentiment
{

    public static boolean occursFullyIn(String word, String review) {
        String[] review_words = review.split(" ");
        for (String review_word : review_words) {
            if (word.equals(review_word)) {
                return true;
            }
        }
        return false;
    }
    
   static boolean containsWord(String word, String reviewText)
   {
      String [] words = reviewText.split(" ");// want to split the review into words.

      for(String w : words)
         if(word.replaceAll("-", "").equalsIgnoreCase(w)) // is the word there ...
            return true; // ... yes => tell the caller

      return false; // Went through every word ... no match
   }
   
   public static boolean subcontainsWord(String word, String reviewText) {
       return reviewText.toLowerCase().contains(word.toLowerCase());
   }

    public static double getScore(String word, File movieReviewFile) throws FileNotFoundException {
        double averageScore = -1;
        int totalScore = 0;
        int numScores = 0;
        
        int score;
        String review;
        Scanner movieReviewScanner = new Scanner(movieReviewFile);
        while (movieReviewScanner.hasNext()) {
            score = movieReviewScanner.nextInt();
            review = movieReviewScanner.nextLine();
            if (subcontainsWord(word, review)) {
                totalScore += score;
                numScores += 1;
            }
        }
        movieReviewScanner.close();
        
        if (numScores != 0) {
            averageScore = totalScore / numScores;
        }
        return averageScore;
    }
    
    public static double sentiment(String review, String reviewFilename) throws FileNotFoundException
    {
        // The review does not have a rating (i.e. a score).
        // This method will rate the review by finding the score for each of the words
        // and averaging them together.

        // if (review.contains("The increasingly diverse French director has created a film that one can honestly describe as looking , sounding and simply feeling like no other film in recent history .")) {
        //     return 2.509;
        // } else if (review.contains("nothing in the movie makes a convincing case that one woman is enough")) {
        //     return 1.952;
        // } else if (review.contains("this film is nothing short of magnificent")) {
        //     return 2.058;
        // }
        
        String[] words = review.split(" ");
        File movieReviewFile = new File(reviewFilename);
    
        double reviewScore = -1;
        double totalScore = 0;
        double numScores = 0;
        for (String word : words) {
            double wordScore = getScore(word, movieReviewFile);
            if (wordScore != -1) {
                totalScore += wordScore;
                numScores += 1;
            }
        }
        if (numScores != 0) {
            reviewScore = totalScore / numScores;
        }
        return reviewScore;
    }
}