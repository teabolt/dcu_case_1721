
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
    public int getFrequentRenterPoints(Rental rental){
            int points = 1;
            if ((rental.getMovie().getPriceCode() == Movie.NEW_RELEASE) && rental.getDaysRented() > 1) points ++;
            return points;
    }

    public String statement(){
        // String output = "Statement for " + getName()  + "\n";
        String output = "";
        double total = 0;
        int frequentRenterPoints = 0;
        for(Rental rental : getRentals())
        {
            double charge = rental.getCharge();
            output += "  " + rental.getMovie().getTitle() + "  " + charge + "\n";
            
            total += charge;
            frequentRenterPoints += rental.getFrequentRenterPoints();
        }
        output += "Amount owed is " + total + "\n";
        output += "You earned " + frequentRenterPoints + " frequent renter points\n";
        return output;
    }
    public double getTotalCharge(){
        double total = 0;
        for(Rental rental : getRentals())
        {
            total += rental.getCharge();
        }
        return total;
    }
    
    public int getTotalFrequentRenterPoints(){
        int frequentRenterPoints = 0;
        for(Rental rental : getRentals())
        {
            frequentRenterPoints += rental.getFrequentRenterPoints();
        }
        return frequentRenterPoints;
    }
    
}