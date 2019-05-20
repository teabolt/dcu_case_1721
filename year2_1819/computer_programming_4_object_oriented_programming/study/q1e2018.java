import java.util.List;
import java.util.ArrayList;

public class q1e2018 {

    public static int negativeBalances(List<BankAccount> accounts) {
        int count = 0;
        for (BankAccount account : accounts) if (account.getBalance() < 0) count += 1;
        // accounts.forEach((account) -> { count += 1; });
        return count;
    }

    public static void main(String[] args) {
        List<BankAccount> accounts = new ArrayList<>();
        accounts.add(new BankAccount(1000));
        accounts.add(new BankAccount(-1000));
        accounts.add(new BankAccount(-0.1));
        accounts.add(new BankAccount(0.1));
        System.out.println(negativeBalances(accounts));
    }

}

class BankAccount{   
    private double balance;   

    public BankAccount(double b)   { this.balance = b;   }   

    public double getBalance() { return balance; }
}