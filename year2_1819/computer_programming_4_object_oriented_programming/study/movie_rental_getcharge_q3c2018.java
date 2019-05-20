class Rental {
    public Rental(Movie movie, int daysRented) {
        this.movie = movie;
        this.daysRented = daysRented;
    }

    public int getDaysRented() { return daysRented; }
    
    public Movie getMovie() { return movie; }

    public String toString() {
        return getMovie() + " [" + getDaysRented() + "]";
    }

    private int daysRented;
    private Movie movie;

    public double getCharge() {
        return getMovie().getCharge(getDaysRented());
    }
}


class Movie {
    public static final int CHILDRENS = 2;
    public static final int REGULAR = 0;
    public static final int NEW_RELEASE = 1;

    public Movie(String title, int priceCode) {
        this.title = title;
        this.priceCode = priceCode;
    }
    
    public int getPriceCode() { return priceCode; }
    public void setPriceCode(int newCode) { priceCode = newCode; }
    public String getTitle() { return title; }

    private int priceCode;
    private String title;

    public double getCharge(int daysRented) {
        double amount = 0.0;
        switch (getPriceCode()) {
            case REGULAR:
                amount += 2;
                if (daysRented > 2)
                    amount += (daysRented-2) * 1.5;
                break;
            case NEW_RELEASE:
                amount += daysRented * 3;
                break;
            case CHILDRENS:
                amount += 1.5;
                if (daysRented > 3)
                    amount += (daysRented-3) * 1.5;
                break;
        }
        return amount;
    }
}