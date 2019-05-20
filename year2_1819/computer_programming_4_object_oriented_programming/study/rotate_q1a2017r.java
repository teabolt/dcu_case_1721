class StrUtils {

    public static String rotate(String s) {
        int N = s.length();
        String last = String.valueOf(s.charAt(N-1));
        String chop = s.substring(0, N-1);
        return last + chop;
    }
}


public class rotate_q1a2017r {

    public static void main(String[] args) {
        System.out.println(StrUtils.rotate("abc"));
    }
}