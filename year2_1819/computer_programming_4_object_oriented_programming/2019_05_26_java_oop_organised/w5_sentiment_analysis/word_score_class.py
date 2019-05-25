
public class WordScore
{
    public String word;
    public int score;
    
    public WordScore(String word) {
        this.word = word;
    }
    
    public boolean in_review(String review_sentence) {
        String[] words = review_sentence.split(" ");
        for (String word : words) {
            if (this.word.equals(word)) {
                return true;
            }
        }
        return false;
    }
    
    public int score(String review) {
        String[] review_contents = review.trim().split(" ", 2);
        int review_score = Integer.parseInt(review_contents[0]);
        String review_sentence = review_contents[1];
        
        int word_score = -1;
        if (in_review(review_sentence)) {
            word_score = review_score;
        }
        return word_score;
    }
}