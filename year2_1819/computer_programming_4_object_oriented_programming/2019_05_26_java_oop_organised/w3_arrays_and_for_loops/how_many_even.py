
public class Test
{
    // Create a static method called countEven which returns the number of even numbers in the array
    static int countEven(int [] numbers)
    {
        int count = 0;
        for(int i = 0; i < numbers.length; i++)
        {
            if (numbers[i] % 2 == 0) {
                count++;
            }
        }
        return count;
    }
}