
 import java.util.List;
 
 class Customer {
     
    private String _name;
    private List<Rental> _rentals;
    
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
    public String statement(){
        double totalAmount = 0;
        int frequentRenterPoints = 0;
        String result = "";
        for (Rental rental : getRentals()) {
            double thisAmount = getTotal(rental);
            // add frequent renter points
            frequentRenterPoints ++;
            // add bonus for a two day new release rental
            if ((rental.getMovie().getPriceCode() == Movie.NEW_RELEASE) && rental.getDaysRented() > 1) frequentRenterPoints ++;
            //show figures for this rental
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