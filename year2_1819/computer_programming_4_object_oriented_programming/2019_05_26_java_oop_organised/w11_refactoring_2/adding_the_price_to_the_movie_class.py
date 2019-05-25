
 public class Movie {
     
    private String _title;
    public Price price;
    
    public Movie(String title, int priceCode) {
        _title = title;
        setPriceCode(priceCode);
    }
    
    public void setPriceCode(int priceCode) {
        switch (priceCode) {
            case Price.NEW_RELEASE:
                price = new NewReleasePrice();
                break;
            case Price.REGULAR:
                price = new RegularPrice();
                break;
            case Price.CHILDRENS:
                price = new ChildrensPrice();
                break;
        }
    }
    
    public String getTitle (){
        return _title;
    }
    
}
