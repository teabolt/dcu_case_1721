
// Create a Word class with one static method called showLetters
public class Word{
    static boolean containsLetter(String word, char letter){
        for(int i = 0; i < word.length(); i++)
        {
            if(word.charAt(i) == letter)
            {
                return true;
            }
        }
        return false;
    }
    
    static String showLetters(String word, String guesses) {
        String show = "";
        for(int i = 0; i < word.length(); i++){
            if (containsLetter(guesses, word.charAt(i))) {
                show += word.charAt(i);
            } 
            else {
                show += "_";
            }
        }
        return show;
    }
}