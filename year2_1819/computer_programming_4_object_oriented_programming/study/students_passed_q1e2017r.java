import java.util.List;
import java.util.ArrayList;

class Student {
    String name;
    int mark;

    public Student(String n, int m) {
        name = n;
        mark = m;
    }

    public static int numberPassed(List<Student> students) {
        int count = 0;
        for (Student stud : students) if (40 <= stud.mark) count += 1;
        return count;
    }
}


public class students_passed_q1e2017r {

    public static void main(String[] args) {
        List<Student> students = new ArrayList<>();
        students.add(new Student("Aha", 40));
        students.add(new Student("Baba", 39));
        students.add(new Student("Sasa", 41));
        System.out.println(Student.numberPassed(students));
    }
}