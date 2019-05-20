public class TestBankAccount
{
   public static void main(String [] args)
   {
      BankAccount currentAccount = new BankAccount();

      currentAccount.balance = 60.05;

      System.out.println("The balance is " + currentAccount.balance);

      currentAccount.balance = currentAccount.balance + 10;

      System.out.println("The balance is " + currentAccount.balance);
   }
}