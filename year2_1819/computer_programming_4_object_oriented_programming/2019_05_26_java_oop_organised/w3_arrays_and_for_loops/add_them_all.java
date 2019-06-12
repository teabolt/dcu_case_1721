
public class Test
{
    // Create a static method called getSum which sums an array of ints
    static int getSum(int [] numbers)
    {
        int sum = 0;
        for(int i = 0; i < numbers.length; i++)
        {
            sum += numbers[i];
        }
        return sum;
    }
}