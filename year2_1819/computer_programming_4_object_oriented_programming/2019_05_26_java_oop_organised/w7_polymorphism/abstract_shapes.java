
import java.util.stream.Stream;

public class Average 
{
    public static double averageArea(Shape[] shapes) {
        
        // double sum = DoubleStream.of(shapes.area()).sum();
        // double sum = StreammapToDouble(shape -> shape.area()).sum();
        double sum = 0;
        for (Shape shape : shapes) {
            sum += shape.area();
        }
        int number = shapes.length;
        double average = 0.0;
        if (0 < number) {
            average = sum / number;
        }
        return average;
    }
}