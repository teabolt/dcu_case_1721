
import java.util.Scanner;

public class Temp {
	public static void main(String [] args)
	{
		System.out.print("Give me a Fahrenheit temperature: ");
		Scanner input = new Scanner(System.in);
		double fahr = input.nextDouble();
		System.out.printf("In Celsius that would be: %f\n",Convert.fahr2cels(fahr));
	}
}
