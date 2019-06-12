
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
    
}