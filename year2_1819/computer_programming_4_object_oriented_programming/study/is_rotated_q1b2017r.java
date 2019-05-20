class StrUtils {

    public static String rotate(String s) {
        int N = s.length();
        String first = String.valueOf(s.charAt(0));
        String chop = s.substring(1, N);
        return chop + first;
    }

    public static boolean isRotated(String s1, String s2) {
        return rotate(s1).equals(s2);
    }
}


public class is_rotated_q1b2017r {

    public static void main(String[] args) {
        System.out.println(StrUtils.isRotated("hell", "ellh"));
    }
}