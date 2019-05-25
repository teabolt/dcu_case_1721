
// Create a Word class with one static method called showLetter
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
    
    static String showLetter(String word, char guess){
        String show = "";
        for(int i = 0; i < word.length(); i++){
            if(word.charAt(i)==guess){
                show += word.charAt(i);
            }
            else{
                show += "_";
            }
        }
        return show;
    }
}