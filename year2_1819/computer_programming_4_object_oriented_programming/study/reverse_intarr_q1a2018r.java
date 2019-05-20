public class reverse_intarr_q1a2018r {

    public static void main(String[] args) {
        int[] nums = {1, 2, 5, 8, -1};
        Test.reverse(nums);
        for (int num : nums) System.out.println(num);
        // String[] strings = {"hi", "bye", "world"};
        // Test.reverse(strings);
        // for (String str : strings) System.out.println(str);
    }
}


class Test {

    public static <T> void reverse(int[] nums) {
        int N = nums.length;
        for (int i = 0; i < N/2; i++) {
            swap(nums, i, N-1-i);
        }
    }

    public static void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}