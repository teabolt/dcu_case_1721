public class q1a2018 {

    public static double average(int[] numarr) {
        int N = numarr.length;
        int sum = 0;
        for (int num : numarr) sum += num;
        double mean = 0;
        if (0 < N) mean = (double) sum/N;
        return mean;
    }

    public static void main(String[] args) {
        int[] num = {2, 3};
        double avg = average(num);
        System.out.println(avg);
        int[] num2 = {};
        double avg2 = average(num2);
        System.out.println(avg2);
    }
}