public class string {
    public static int sub_occurs(String w, String s) {
        int occurrences = 0;
        // System.out.println(w.length());
        // System.out.println(s.length());
        for (int i = w.length(); i <= s.length(); i++) {
            // System.out.println((i-w.length()) + ", " + i + ", " + s.substring(i-w.length(), i));
            if (w.equals(s.substring(i-w.length(), i))) {
                occurrences += 1;
            }
        }
        return occurrences;
    }

    public static void main(String[] args) {
        // String s = "hello there hellow hello";
        // String w = "hello";
        // // int i = w.length();
        // // System.out.println(s.substring(i, i+w.length()));
        // System.out.println(sub_occurs("hello", "hello there hellow hello"));
        String s = " 2 Massoud 's story is an epic , but also a tragedy , the record of a tenacious , humane fighter who was also the prisoner -LRB- and ultimately the victim -RRB- of history .";
        String[] a = s.trim().split(" ", 2);
        System.out.println(a[0] + ", " + a[1]);
    }
}