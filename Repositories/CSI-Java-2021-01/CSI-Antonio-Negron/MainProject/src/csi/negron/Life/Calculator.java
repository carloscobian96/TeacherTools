package csi.negron.Life;

import java.util.ArrayList;
import java.util.List;

public class Calculator {
	public static void main(String[] args) throws InterruptedException {
		double startingAmount = 2000;
		double cash = 0.0;
		cash += startingAmount;
		double invested = 0;
		int lifeExpectancy = 81;

		for (int age = 0; age < lifeExpectancy; age++) {
			int numberOfYears = age;
			List<Loans> loans = new ArrayList<Loans>();
//loans.add(new Loans("Student Loans", 0, 0.466, 0, age,numberOfYears));
			loans.add(new Loans("Personal Loans", 0, 0.16, 0, age, numberOfYears));
			loans.add(new Loans("Mortgage Loans", 0, 0.3125, 0, age, numberOfYears));
			loans.add(new Loans("Credit Card", 0, 0.29, 0, age, numberOfYears));

// highschool
			if (age <= 18) {
				String location = "PR";
				double salary = 0;
				cash += salary;

			} else if (age <= 22) { //// Uconn Bachelors
				String location = "Connecticut";
				double salary = 0;
				double tuition = 40_000 + 4_000 - 30_066;
				double costofLiving = 14_000; // food, housing, bills.

				cash += salary;
				loans.get(0).principal += tuition;
				loans.get(0).principal += costofLiving;
				loans.get(0).differed = true;
			} else if (age <= 26) { //// Medschool Johns Hopkins
				String location = "Baltimore";
				double salary = 0;
				double tuition = 54_000 + 4_000 - 48_000;
				double costofLiving = 14_000; // food, housing, bills.

				cash += salary;
				loans.get(0).principal += tuition;
				loans.get(0).principal += costofLiving;
				loans.get(0).differed = true;

			} else if (age <= 27) { // residencia
				String location = "IN";
				double salary = 64_000 * 0.9;
				double tuition = 390;
				double costofLiving = 30_000; // food, housing, bills, car stuff, and literally everything.

				cash += salary;
				loans.get(0).principal += tuition;
				loans.get(0).principal += costofLiving;
				loans.get(0).differed = true;
// debt += -((loanInterest * debt) * 12);

			} else if (age <= 31) { // specialty in Cardiovascular Surgery
				String location = "IN";
				double salary = 227_000 * 0.9;
				double tuition = 36_000;
				double costofLiving = 70_000; // food, housing, bills, car stuff.

				cash += salary;

				loans.get(0).principal += tuition;
				loans.get(0).principal += costofLiving;
				loans.get(0).differed = true;
// debt += -((loanInterest * debt) * 12);

			} else if (age <= 34) { // Cardiovascular Surgeon
				String location = "IN";
				double salary = 700_000 * 0.9;
				double costofLiving = 260_000; // food, housing, bills, car stuff.

				cash += salary;
				cash -= costofLiving;
				loans.get(0).differed = false;
// debt += -((loanInterest * debt) * 12);

			} else if (age <= 66) { // retire
				String location = "IN";
// salary is actually my retirement pay
				double salary = 2_000 * 0.9;
// double investment = 1000;
// double investmentInterest = 0.40;
				double costofLiving = 50_000; // food, housing, bills, car stuff.

				cash += salary;
				cash += costofLiving;

			} else if (age <= 82) {
// be with the family
				String location = "IN";
				double salary = 1_000 * 0.9;
				double costofLiving = 20_000; // food, housing, bills, car stuff.

				cash += salary;
				cash -= costofLiving;
			}
// Car

			else if (age == 30 && cash > 30_000) {
				double newCarPrice = 50_000;
				double downPayment = newCarPrice * 0.15;
				double interestRate = 0.05;
				int repaymentYears = 6;

				Loans carLoan = new Loans("Car Loan", (newCarPrice - downPayment), interestRate, repaymentYears);
				loans.add(carLoan);

				System.out.println("Monthly car Payment: " + carLoan.getMonthlyPayment() + " For a total of "
						+ carLoan.getTotalPayment());
			}
//Car
			else if (age == 45 && cash > 50_000) {
				double newCarPrice = 100_000;
				double downPayment = newCarPrice * 0.15;
				double interestRate = 0.05;
				int repaymentYears = 5;

				Loans carLoan = new Loans("Car Loan", (newCarPrice - downPayment), interestRate, repaymentYears);
				loans.add(carLoan);
				System.out.println("Monthly car Payment: " + carLoan.getMonthlyPayment() + " For a total of "
						+ carLoan.getTotalPayment());
			}
// expensive house.
			if (age == 34 && cash > 200_000) {
				double newHousePrice = 350_000;
				double downPayment = 150_000;

				double interestRate = 0.05;
				double payment = 2_000;

				loans.add(new Loans("House Loan", (newHousePrice - downPayment), interestRate, payment, age,
						numberOfYears));
			}

// -----=====88888=====-----
// Loans
// -----=====88888=====-----
// Monthly loan payments
			for (Loans loan : loans) {
				for (int month = 0; month < 12; month++) {
					if (loan.getBalance() > 0 && loan.differed == false) {
						cash -= loan.makePayment();
					}
				}
			}

//Calculate Debt Balance
			double debt = 0;
			for (Loans loan : loans)
				debt += loan.principal;

// Output year-end review
			System.out.println("Balance at age: " + age + " is: " + cash + " with a debt of " + debt + " and "
					+ invested + " invested.");
// Did you make it?
			if (age > 30 && cash < 0) {
				System.out.println("You died!");
			}

			if (age > 79 && cash > 0) {
				System.out.println("You Survived");
				break;
			}

		}
	}
}
