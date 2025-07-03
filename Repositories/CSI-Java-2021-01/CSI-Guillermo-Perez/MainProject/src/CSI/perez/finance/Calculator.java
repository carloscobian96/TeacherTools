
package csi.perez.finance;

import java.util.*;

public class Calculator {

	private static double askForMoney(double amount) {

		System.out.println("You have been spared by someone who gave you: " + amount);
		return amount;
	}

	public static void main(String[] args) throws InterruptedException {

		double initial = 2000;
		double cash = 0;

		List<Loan> loans = new ArrayList<Loan>();

		loans.add(new Loan("Student Loans", 0, 0.0466, 30));
		loans.add(new Loan("Personal Loans", 0, 0.16, 10));
		loans.add(new Loan("Mortgage Loans", 0, 0.03125, 30));
		loans.add(new Loan("CreditCard", 0, 0.29, 70));

		cash += initial;

		for (int age = 0; age <= 70; age++) {

// formative years
			if (age <= 18) {
				double salary = 0;
				cash += salary;

// Engineering masters and Baccalaureate
			} else if (age <= 24) {
				String location = "New Mexico";
				double salary = 7_728;
				// Tuition + fees - scholarship
				double tuition = 22_801 + 1_698;
				// Housing fees
				double costOfLiving = 14_000;

				cash += salary;
				cash -= costOfLiving;
				cash += askForMoney(costOfLiving);
				loans.get(0).principal += tuition;
				loans.get(0).differed = true;

			}

// Work as a starting Nuclear Engineer in a studio apartment
			else if (age <= 28) {
				loans.get(0).differed = false;
				String Location = "Oklahoma";
				// Salary -10% tax
				double salary = 57_870 * 0.9;
				// Studio apartment + electricity + water + wi-fi bills
				double rent = 950 + 55 + 40 + 35;
				// 60$ daily food stipend
				double food = 60 * 365;
				// Car expenses
				double carExpenses = 60 * 12 + 1_000;
				double loanInterest = 0.049;

				cash = salary;
				cash -= food;
				cash -= rent;
				cash -= carExpenses;
			}
// Work as a Mid-level Nuclear Engineer in second house
			else if (age <= 32) {
				String Location = "Oklahoma";
				// Salary -10% tax
				double salary = 116_140 * 0.9;
				// 60$ daily food stipend
				double food = 80 * 365;
				// Car expenses
				double carExpenses = 60 * 12 + 1_000;
				double loanInterest = 0.049;

				cash += salary;
				cash -= food;
				cash -= carExpenses;
			}
// Work as an Senior  Nuclear Engineer
			else if (age <= 36) {
				String Location = "Oklahoma";
				// Salary -10% tax
				double salary = 134_575 * 0.9;
				// 60$ daily food stipend
				double food = 80 * 365;
				// Car expenses
				double carExpenses = 60 * 12 + 1_000;
				double loanInterest = 0.049;

				cash += salary;
				cash -= food;
				cash -= carExpenses;
			}

// Work as an Top-level  Nuclear Engineer
			else if (age <= 40) {
				String Location = "Oklahoma";
				// Salary -10% tax
				double salary = 167_080 * 0.9;
				// 60$ daily food stipend
				double food = 80 * 365;
				// Car expenses
				double carExpenses = 60 * 12 + 1_000;
				double loanInterest = 0.049;

				cash += salary;
				cash -= food;
				cash -= carExpenses;
			}
//Loans
			for (Loan loan : loans) {
				// Carry out 12 payments (monthly)
				for (int month = 0; month < 60; month++) {
					// If this loan is still due and has not been differed
					if (loan.getBalance() > 0 && loan.differed == false) {
						cash -= loan.makePayment();
					}
				}
			}



//				Additional logic
//Car
			// For college I will not be using a car, I will be walking since I live on
			// campus
			// Bought a used car at 24 after finishing college and starting work as a noobie
			// Nuclear Engineer
			if (age == 24 && cash >= 15_000) {
				double usedCarPrice = 10_000;
				cash -= usedCarPrice;
				System.out.println("Bought a car for: " + usedCarPrice);
			}

			// Bought a new car at 32 as a mid-level Nuclear Engineer

			if (age == 32 && cash < 70_000 && cash > 40_000) {
				double newCarPrice = 64_000;
				double downPayment = 64_000 * 0.15;
				double interestRate = 0.05;
				int repaymentYears = 8;

				Loan carLoan = new Loan("Car Loan", (newCarPrice - downPayment), interestRate, repaymentYears);
				loans.add(carLoan);

				System.out.println("Monthly car Payment: " + carLoan.getMonthlyPayment() + " For a total of "
						+ carLoan.getTotalPayment());
			}
			// Car should last me at least more than 15 years so no need to buy another one

//House
			// Bought a House at 35 as a mid-level Nuclear Engineer
			if (age == 35 && cash > 220_000) {
				double housePrice = 205_000;
				double downPayment = housePrice * 0.15;
				double interestRate = 0.03;
				int repaymentYears = 25;

				Loan mortgageLoan = new Loan("My first home", (housePrice - downPayment), interestRate, repaymentYears);
				loans.add(mortgageLoan);

				System.out.println("House mortgage: " + mortgageLoan.getMonthlyPayment() + " For a total of "
						+ mortgageLoan.getTotalPayment());
			}
			
			
			
			// Calculate Debt Balance
			double debt = 0;
			for (Loan loan : loans)
				debt += loan.getBalance();

			double invested = 0;

			System.out.println("Balance at age: " + age + " is: " + cash + " with a debt of " + debt + " and "
					+ invested + " invested.");

			if (cash < 0) {
				System.out.println("Out of cash. You Died!");
				break;
			}

//			End For Loop
		}
	}
}
