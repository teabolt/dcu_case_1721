
public class BankAccount
{
	public double balance;

	public BankAccount(double b) {
		balance = b;
	}

	public BankAccount() {
		balance = 100.0;
	}

	public void withdraw(double amount) {
		balance -= amount;
	}

	public void deposit(double amount) {
		balance += amount;
	}

	public String toString(BankAccount this) {
		return "The balance is " + this.balance;
	}

	public void setBalance(double amount) {
		balance = amount;
	}

	public double getBalance() {
		return balance;
	}
}