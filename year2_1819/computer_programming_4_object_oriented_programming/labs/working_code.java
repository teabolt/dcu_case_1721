import java.util.Scanner;
import java.io.FileNotFoundException;
import java.io.File;

public class Sentiment
{
    public static double sentiment(String review, String reviewFilename) throws FileNotFoundException
    {
        double totalScore = 0;
        double totalWord = 0;
        String [] rev = review.split(" ");
        for(String word : rev){
            double score = containsWord(word, reviewFilename);
            if(score != 0){
                totalWord++;
                totalScore = totalScore + score;
            }
        }
        
        if(totalWord != 0)
            return totalScore/totalWord;
        else
            return -1;
    }
    
    public static double containsWord(String word, String fileName) throws FileNotFoundException{
        Scanner in = new Scanner(new File(fileName));
        
        double totalRev = 0;
        double totalScore = 0;
        
        while(in.hasNextLine()){
            String line = in.nextLine();
            int score = Integer.parseInt(line.substring(0,1));
            if(word.equals(".") || word.equals(",")){
                if(line.contains(word)){
                    totalRev++;
                    totalScore = totalScore + score;
                }
            }else{
                String [] lines = line.split(" ");
                for(String w : lines){
                    if(w.equals(word)){
                        totalRev++;
                        totalScore = totalScore + score;
                        break;
                    }
                }
            }
        }
        in.close();
        if(totalRev != 0)
            return totalScore/totalRev;
        else
            return 0;
    }
}