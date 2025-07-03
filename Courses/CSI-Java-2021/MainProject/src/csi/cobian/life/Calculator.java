package csi.cobian.life;

import java.text.DecimalFormat;
import java.util.*;

public class Calculator {

	// private static final DecimalFormat df = new DecimalFormat("#.##");

	public static void main(String[] args) throws InterruptedException {

		double initial = 15_000;
		double cash = 0;
		double invested = 0;

		List<Loan> loans = new ArrayList<Loan>();

		loans.add(new Loan("Student Loans", 0, 0.0466, 30));
		loans.add(new Loan("Personal Loans", 0, 0.16, 10));
		loans.add(new Loan("Mortgage Loans", 0, 0.03125, 30));
		loans.add(new Loan("CreditCard", 0, 0.29, 99));

		cash += initial;

		for (int age = 0; age <= 80; age++) {

			// -----=====88888=====-----
			// Lifetime accounting
			// -----=====88888=====-----

			// Formative Years
			if (age < 18) {
				double salary = 0;
				cash += salary;
			}
			// Biology Baccalaureate
			else if (age < 23) {
				String location = "IN";

				double salary = 0;
				// Tuition + fees - scholarship
				double tuition = 54_000 + 4_000;
				// rent + food + expenses
				double costOfLiving = 17_000;

				cash += salary;

				// Federal Loans are waived while you study.
				loans.get(0).principal += costOfLiving;
				loans.get(0).principal += tuition;
				loans.get(0).differed = true;

			}
			// med school
			else if (age < 27) {
				String location = "IN";

				double salary = 0;
				// Tuition + fees - scholarship
				double tuition = 55_000 + 4_000;
				// House rent + food + expenses
				double costOfLiving = 1_200 * 12 + 500 * 12 + 1_000 * 12;

				cash += salary;

				loans.get(0).principal += costOfLiving;
				loans.get(0).principal += tuition;
			}
			// Residency
			else if (age < 33) {
				loans.get(0).differed = false;
				
				String location = "IN";

				double salary = 64_000;
				double costOfLiving = 36_000;

				cash += salary;
				cash -= costOfLiving;
			}
			// Work
			else if (age < 65) {
				double salary = 200_000;
				cash += salary;
			}
			// Retirement
			else {
			}

			// -----=====88888=====-----
			//		Additional Logic
			// -----=====88888=====-----

		// Buy a used car after college. Could you afford it? 
		if(age == 24 && cash >= 15_000) {
		        double usedCarPrice = 5_000.00;
		        cash -= usedCarPrice;

		        System.out.println("Bought a car for: " + usedCarPrice);
		} // New cars with loan interest are a bad investment! 
		else if(age == 24 && cash < 15_000) {
		        double newCarPrice = 35_000;
		        double downPayment = 5_000;
		        double interestRate = 0.05;
		        int repaymentYears = 6;

		        Loan carLoan = new Loan("Car Loan", 
		                  (newCarPrice - downPayment), 
		                  interestRate, 
		                  repaymentYears);
		        loans.add( carLoan );

		        System.out.println("House mortgage: " + carLoan.getMonthlyPayment() + " For a total of " + carLoan.getTotalPayment() );
		}


		// -----=====88888=====-----
//     Additional Logic
// -----=====88888=====-----

// Buy a House at 35
if(age == 35 && cash >= 200_000){
	double cashPrice = 150_000;
	cash -= cashPrice;

	System.out.println("Bought a House for: " + cashPrice);
}
else if(age == 35 && cash >= 100_000){
	double apartmentPrice = 75_000;
	cash -= apartmentPrice;

	System.out.println("Bought an  Apartment for: " + apartmentPrice);
}
else if(age == 35 &&  cash > 15_000){
	double apartmentPrice = 75_000;
	double downPayment = apartmentPrice * 0.15;
	double interestRate = 0.03;
	// int repaymentYears = 15;
	int repaymentYears = 30;

	Loan mortgageLoan = new Loan("My first home", 
			(apartmentPrice - downPayment),
			interestRate, 
			repaymentYears);
	loans.add( mortgageLoan );

	System.out.println("House mortgage: " + mortgageLoan.getMonthlyPayment() + " For a total of " + mortgageLoan.getTotalPayment() );
}

			// -----=====88888=====-----
			//           Loans
			// -----=====88888=====-----

			// Iterate over all loans
			for (Loan loan : loans) {
				// Carry out 12 payments (monthly)
				for (int month = 0; month < 12; month++) {
					// If this loan is still due and has not been differed
					if (loan.getBalance() > 0 && loan.differed == false) {
						cash -= loan.makePayment();
					}
				}
			}

			// Calculate Debt Balance
			double debt = 0;
			for (Loan loan : loans)
				debt += loan.getBalance();

			// Output year-end review
			System.out.println("Balance at age: " + age + " is: " + cash + " with a debt of " + debt + " and "
					+ invested + " invested.");

			// Did you make it?
			if (cash < 0) {
				System.out.println("Out of cash. You Died!");
				break;
			}
		}
	}

	private static double askForMoney(double amount) {
		System.out.println("You have been saved by someone who gave you: " + amount);
		return amount;
	}
}
