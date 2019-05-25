
// create a Swap class with one method called swap which use templates to swap two elements of an array.
// It should have be three parameters, the first is the array and the next two are the indices of the elements to be swapped.
public class Swap{
    public static <T> void swap(T [] a,int index1, int index2){
        T tmp = a[index1];
        a[index1]= a[index2];
        a[index2]= tmp;
    }
}