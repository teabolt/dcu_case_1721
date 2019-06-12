
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Sentiment
{

   static boolean containsWord(String word, String reviewText)
   {
      if (word.equals(".") || word.equals(",")) {
          return reviewText.contains(word);
      }
      else {
          String [] words = reviewText.split(" ");
    
          for(String w : words)
             if(word.equalsIgnoreCase(w))
                return true;
    
          return false;
      }
   }
   
    public static double getScore(String word, File movieReviewFile) throws FileNotFoundException {
        double averageScore = 0;
        double totalScore = 0;
        
        int numScores = 0;

        Scanner movieReviewScanner = new Scanner(movieReviewFile);
        while (movieReviewScanner.hasNext()) {
            int score = movieReviewScanner.nextInt();
            String review = movieReviewScanner.nextLine();
            if (containsWord(word, review)) {
                totalScore += score;
                numScores++;
            }
        }
        movieReviewScanner.close();
        
        if (numScores != 0) {
            averageScore = totalScore / numScores;
        }
        return averageScore;
    }
    
    public static boolean isAverage(double wordScore) {
        return 1.8 <= wordScore && wordScore < 2.2;
    }
    
    public static double sentiment(String review, String reviewFilename) throws FileNotFoundException
    {

        String[] words = review.split(" ");
        File movieReviewFile = new File(reviewFilename);
    
        double reviewScore = -1;
        double totalScore = 0;
        int numScores = 0;
        
        for (String word : words) {
            double wordScore = getScore(word, movieReviewFile);
            if (wordScore != 0 && !isAverage(wordScore)) {
                totalScore += wordScore;
                numScores++;
            }
        }
        if (numScores != 0) {
            reviewScore = totalScore/numScores;
        }
        return reviewScore;
    }
}