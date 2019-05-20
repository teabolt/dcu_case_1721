public class is_reverse_intarr_q1b2018r {

    public static void main(String[] args) {
        int[] nums1 = {1, 2, 5, 4};
        int[] nums2 = {4, 5, 2, 1};
        System.out.println(Test.isReversed(nums1, nums2));
        int[] nums3 = {4, 5, 2, 0};
        System.out.println(Test.isReversed(nums1, nums3));
    }
}


class Test {

    public static boolean isReversed(int[] nums1, int[] nums2) {
        int N = nums1.length;
        if (N != nums2.length) return false; // pre-emptively exit
        for (int i = 0; i < N; i++) {
            int num1 = nums1[i];     // from the front
            int num2 = nums2[N-1-i]; // from the back
            if (num1 != num2) return false; // pre-emptive exit
        }
        return true;
    }
}