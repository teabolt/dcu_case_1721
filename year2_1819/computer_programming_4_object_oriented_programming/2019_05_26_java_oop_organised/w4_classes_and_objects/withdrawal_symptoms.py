
public class BankAccount
{
	public double balance;

	public BankAccount(double b) {
		balance = b;
	}

	public void withdraw(double amount) {
		balance -= amount;
	}
}