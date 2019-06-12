
 abstract class Price {
     final static int REGULAR = 0;
     final static int NEW_RELEASE = 1;
     final static int CHILDRENS = 2;
     abstract int getPriceCode();
     abstract double getCharge(int daysRented);
 }