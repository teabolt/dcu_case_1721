
// Create a Word class with a static method called allDone
public class Word {
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

    static boolean allDone(String word, String guessed) {
        for(int i = 0; i < word.length(); i++) {
            if (!containsLetter(guessed, word.charAt(i))) {
                return false;
            }
        }
        return true;
    }
}