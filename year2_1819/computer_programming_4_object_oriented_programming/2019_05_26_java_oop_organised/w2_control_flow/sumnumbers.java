
import java.util.Scanner;

public class SumNumber {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int number = reader.nextInt();
        int sum = number;
        for (int i = 1; i < number; i++) {
            sum += i;
        }
        System.out.printf("The sum of the numbers from 1 to %d is %d\n", number, sum);
        
    }
}