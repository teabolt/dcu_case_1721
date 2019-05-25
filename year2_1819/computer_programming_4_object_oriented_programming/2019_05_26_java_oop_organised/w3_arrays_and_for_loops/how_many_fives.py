
public class Test
{
    // Create a static method called countFives which returns the number of fives in the array
    static int countFives(int [] numbers)
    {
        int count = 0;
        for(int i = 0; i < numbers.length; i++)
        {
            if (numbers[i] == 5) {
                count++;
            }
        }
        return count;
    }
}