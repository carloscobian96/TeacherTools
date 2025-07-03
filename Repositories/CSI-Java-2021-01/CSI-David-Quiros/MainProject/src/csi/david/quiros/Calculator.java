package csi.david.quiros;
import java.util.*;



public class Calculator {

 

       private static double askForMoney(double amount) {

 

              System.out.println("You have been given " + amount);

              return amount;

       }

 

       public static void main(String[] args) throws InterruptedException {

 

              double initial = 2500;

              double cash = 0;

 

              List<Loan> loans = new ArrayList<Loan>();

 

              loans.add(new Loan("Student Loans", 0, 0.0466, 30));

              loans.add(new Loan("Personal Loans", 0, 0.16, 10));

              loans.add(new Loan("Mortgage Loans", 0, 0.03125, 30));

              loans.add(new Loan("CreditCard", 0, 0.29, 70));

 

              cash += initial;

 

              for (int age = 0; age <= 70; age++) {

 

// formative years
//using my dads car
                     if (age <= 18) {
                    	 String location = "PR";

                           double salary = 0;

                           cash += salary;

 

                     } else if (age <= 24) {
 // college years in Purdue

                           String location = "IN";

                           	double salary = 0;
                           
           					double tuition = 28_000 + 4_000 - 16_000 - 20_000;
           				
           					double costOfLiving = 13_500;


 

                           cash += salary;

                           cash -= costOfLiving;

                           cash += askForMoney(costOfLiving);

                           loans.get(0).principal += tuition;

                           loans.get(0).differed = true;

 

                     }

 //Living life In MA

                     else if (age <= 28) {

                           loans.get(0).differed = false;

                           String Location = "MA";

                           double salary = 94_046 * 1.3; 
           				
           				double costOfLiving = 12 * (2620 + 1000 + 300);
           				
           				double food = 100 * 365; 
           				
           				double rent = 800 + 50 + 60 + 40;
           				
           				double loanInterest = 0.0;
           				
           				double carexpenses = 100 * 12 + 1_000;

 

                           cash = salary;

                           cash -= food;

                           cash -= rent;

                           cash -= carexpenses;

                     }

                     else if (age <= 32) {

                           String Location = "MA";

                           double salary = 134_700 * 0.9;

                           double food = 80 * 365;

                           double carExpenses = 60 * 12 + 1_000;

                           double loanInterest = 0.049;

 

                           cash += salary;

                           cash -= food;

                           cash -= carExpenses;

                     }

                     else if (age <= 36) {

                           String Location = "MA";

                           double salary = 167_080 * 0.9;

                           double food = 80 * 365;

                           double carExpenses = 60 * 12 + 1_000;

                           double loanInterest = 0.049;

 

                           cash += salary;

                           cash -= food;

                           cash -= carExpenses;

                     }

 

                     else if (age <= 40) {

                           String Location = "MA";

                           double salary = 198_020 * 0.9;

                           double food = 80 * 365;

                           double carExpenses = 60 * 12 + 1_000;

                           double loanInterest = 0.049;

 

                           cash += salary;

                           cash -= food;

                           cash -= carExpenses;

                     }

                     for (Loan loan : loans) {

                          

                           for (int month = 0; month < 60; month++) {

                                 

                                  if (loan.getBalance() > 0 && loan.differed == false) {

                                         cash -= loan.makePayment();

                                  }

                           }

                     }

 

 

                     if (age == 24 && cash >= 15_000) {
// used car
                           double usedCarPrice = 10_000;

                           cash -= usedCarPrice;

                           System.out.println("Bought a car for: " + usedCarPrice);

                     }

 

                    

 

                     if (age == 32 && cash < 70_000 && cash > 40_000) {

                           double newCarPrice = 70_000;

                           double downPayment = 70_000 * 0.15;

                            double interestRate = 0.05;

                           int repaymentYears = 9;

 

                           Loan carLoan = new Loan("Car Loan", (newCarPrice - downPayment), interestRate, repaymentYears);

                           loans.add(carLoan);

 

                           System.out.println("Monthly car Payment: " + carLoan.getMonthlyPayment() + " For a total of "

                                         + carLoan.getTotalPayment());

                     }

      

                     if (age == 35 && cash > 220_000) {
//House in MA
                           double housePrice = 110_000;

                           double downPayment = housePrice * 0.15;

                           double interestRate = 0.07;

                           int repaymentYears = 25;

 

                           Loan mortgageLoan = new Loan("My home", (housePrice - downPayment), interestRate, repaymentYears);

                           loans.add(mortgageLoan);

 

                           System.out.println("House mortgage: " + mortgageLoan.getMonthlyPayment() + " For a total of "

                                         + mortgageLoan.getTotalPayment());

                     }

                    

                    

                    

                     double debt = 0;

                     for (Loan loan : loans)

                           debt += loan.getBalance();

 

                     double invested = 0;

 

                     System.out.println("Balance at age: " + age + " is: " + cash + " with a debt of " + debt + " and "

                                  + invested + " invested.");

 

                     if (cash < 0) {

                           System.out.println("You moved back with your mom!!!");

                           break;

                     }

              }

       }

}