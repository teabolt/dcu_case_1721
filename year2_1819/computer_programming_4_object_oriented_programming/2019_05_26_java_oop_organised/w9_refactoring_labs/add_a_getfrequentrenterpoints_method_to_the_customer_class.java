
 import java.util.List;
 
 class Customer {
     
    private String _name;
    private List<Rental> _rentals;
    private int frequentRenterPoints;
    
    public Customer (String name, List<Rental> rentals){
        _name = name;
        _rentals = rentals;
    }
    
    public void addRental(Rental arg) {
        _rentals.add(arg);
    }
    
    public String getName (){
        return _name;
    }
    
    public List<Rental> getRentals(){
        return _rentals;
    }
    public String toString(){
        return getName()+": "+getRentals();
    }
    public double getTotal(Rental rental){
        return rental.getCharge();
    }
    public int getFrequentRenterPoints(Rental rental){
            int points = 1;
            if ((rental.getMovie().getPriceCode() == Movie.NEW_RELEASE) && rental.getDaysRented() > 1) points ++;
            return points;
    }

    public String statement(){
        double totalAmount = 0;
        String result = "";
        for (Rental rental : getRentals()) {
            double thisAmount = getTotal(rental);
            frequentRenterPoints += getFrequentRenterPoints(rental);
            result += "  " + rental.getMovie().getTitle()+ "  " +
            String.valueOf(thisAmount) + "\n";
                totalAmount += thisAmount;
      }
     //add footer lines
     result += "Amount owed is " + String.valueOf(totalAmount) +
    "\n";
     result += "You earned " + String.valueOf(frequentRenterPoints)
    +
    " frequent renter points\n";
     return result;
    }
}