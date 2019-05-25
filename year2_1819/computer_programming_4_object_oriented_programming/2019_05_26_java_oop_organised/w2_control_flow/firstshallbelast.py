
public class Test
{
    // This method returns a String and receives a String
    public static String firstShallBeLast(String word)
    {
        // Reorganise the string.  Remember the '+' operator concatenates strings.
        // Needs to return the correct string.
        String swapped;
        char first = word.charAt(0);
        String middle = word.substring(1, word.length()-1);
        char last = word.charAt(word.length()-1);
        swapped = last + middle + first;
        return swapped;
    }
}