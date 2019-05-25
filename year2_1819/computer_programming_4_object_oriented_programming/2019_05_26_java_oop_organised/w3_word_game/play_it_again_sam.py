
// Write your Hangman class here
import java.util.Scanner;

public class Hangman
{
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        
        // First get the word
        int wordSeed = in.nextInt();

        String word = Word.getWord(wordSeed);

        // Now you have the word ... encourage the user to guess.
        String guesses = "";
        System.out.println("The word is");
        System.out.println(Word.showLetters(word, guesses));
        
        while(!Word.allDone(word, guesses)){
            System.out.println("Guess a letter:");
            char letter = in.next().charAt(0);
            guesses += letter;
            System.out.println(Word.showLetters(word, guesses));
            
        }
        System.out.println("Well Done, the word was " + word + ".");
    }
}