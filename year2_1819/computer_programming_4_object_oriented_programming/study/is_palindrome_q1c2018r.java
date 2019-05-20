class Test {

    public static boolean isPalindrome(String s) {
        int N = s.length();
        for (int i = 0; i < N/2; i++) {
            String frontCh = String.valueOf(s.charAt(i));
            String backCh = String.valueOf(s.charAt(N-1-i));
            if (!frontCh.equals(backCh)) return false;
        }
        return true;
    }
}


public class is_palindrome_q1c2018r {

    public static void main(String[] args) {
        String s1 = "madam";
        String s2 = "abcddcbz";
        System.out.println(Test.isPalindrome(s1));
        System.out.println(Test.isPalindrome(s2));
    }
}