
public class Test
{
    // Create a static void method called reverse which takes an array of ints
    static int [] reverse(int [] numbers)
    {
        int tmp;
        for(int i = 0; i < numbers.length/2; i++)
        {
            tmp = numbers[i];
            numbers[i] = numbers[numbers.length-i-1];
            numbers[numbers.length-i-1] = tmp;
        }
        return numbers;
    }
}