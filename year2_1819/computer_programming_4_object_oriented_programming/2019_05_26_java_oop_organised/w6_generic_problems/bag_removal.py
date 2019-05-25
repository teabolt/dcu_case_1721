
@SuppressWarnings("unchecked")
public class Bag<T>
{
   private T[] bag = (T[])(new Object[100]);
   private int numElements = 0;
   
   public void add(T x)
   { // put x in bag
      bag[numElements] = x;
      numElements++;
   }
   
   public void remove(T x){
        int i = 0;
        while (i < length() && !bag[i].equals(x)) i++;
        if (i < length()) {
            T[] newBag = (T[]) (new Object[100]);
            for (int j = 0; j < i; j++) {
                newBag[j] = bag[j];
            }
            for (int j = i; j < newBag.length-1; j++) {
                newBag[j] = bag[j+1];
            }
            bag = newBag;
            // bag[i] = (T) new Object();
            numElements--;
        }
   }
   
   public int count(T x)
   {
      int count = 0;
      for (int i=0; i<numElements; i++)
         if (bag[i].equals(x)) // .equals because T a class 
            count++;
      return count;
   }

   public int length()
   {
      return numElements;
   }
}