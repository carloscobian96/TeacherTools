package csi.evaluation;

import java.util.ArrayList;
import java.util.List;

public class Calculator {
	public static void main(String[] args) throws InterruptedException {
		double startingAmount = 1000;
		double cash = 0.0;
	    cash += startingAmount;
		double invested = 0;
	    int lifeExpectancy = 81;

		for (int age = 0; age < lifeExpectancy; age++) {

			int numberOfYears = age;

			List<Loan> loans = new ArrayList<Loan>();
			loans.add(new Loan("Student Loans", 0, 0.466, 0, age,numberOfYears));
			loans.add(new Loan("Personal Loans", 0, 0.16, 0, age, numberOfYears));
			loans.add(new Loan("Mortgage Loans", 0, 0.3125, 0, age, numberOfYears));
			loans.add(new Loan("Credit Card", 0, 0.29, 0, age, numberOfYears));

			// highschool			
			    if (age <= 18) {
				String location = "PR";
				double salary = 10_000;
				cash += salary;

			} else if (age <= 23) { //// medschool florida University of Miami
				String location = "MI";
				double salary = 17_000 * 0.9;
				double tuition = 52_000 + 4_000 - 30_066; // poor moment
				double costofLiving = 14_000; // food, housing, bills, car stuff, and literally everything.

				cash += salary;
				loans.get(0).principal += tuition;
				loans.get(0).principal += costofLiving;
				loans.get(0).differed = true;
			} else if (age <= 27) { // residencia
				String location = "MI";
				double salary = 64_000 * 0.9;
				double tuition = 390;
				double costofLiving = 54_000;  // food, housing, bills, car stuff, and literally everything.

				cash += salary;
				loans.get(0).principal += tuition;
				loans.get(0).principal += costofLiving;
				loans.get(0).differed = true;
//				debt += -((loanInterest * debt) * 12);
			} else if (age <= 30) { // specialty
				String location = "MI";
				double salary = 80_000 * 0.9;
				double tuition = 0;
				double costofLiving = 70_000; // food, housing, bills, car stuff, and literally everything.

				cash += salary;

				loans.get(0).principal += tuition;
				loans.get(0).principal += costofLiving;
				loans.get(0).differed = true;
//				debt += -((loanInterest * debt) * 12);

			} else if (age <= 34) { // work
				String location = "MI";
				double salary = 340_000 * 0.9;
				double costofLiving = 260_000; // food, housing, bills, car stuff, and literally everything.

				cash += salary;
				cash -= costofLiving;
				loans.get(0).differed = false;
//				debt += -((loanInterest * debt) * 12);

			} else if (age <= 65) { // retire
				String location = "MI";
				// salary is actually my retirement pay
				double salary = 2_000 * 0.9;
				// double investment = 1000;
				// double investmentInterest = 0.40;
				double costofLiving = 15_000; // food, housing, bills, car stuff, and literally everything.

				cash += salary;
				cash += costofLiving;

			} else if (age <= 82) {
				// be with the family
				String location = "MI";
				double salary = 1_000 * 0.9;
				double costofLiving = 20_000;  // food, housing, bills, car stuff, and literally everything.

				cash += salary;
				cash -= costofLiving;
			}
			// Pickop troc
			// I be insta buying
			else if (age == 30 && cash > 30_000) {
				double newCarPrice = 50_000;
				double downPayment = newCarPrice * 0.15;
				double interestRate = 0.05;
				int repaymentYears = 6;

				Loan carLoan = new Loan("Car Loan", (newCarPrice - downPayment), interestRate, repaymentYears);
				loans.add(carLoan);

				System.out.println("Monthly car Payment: " + carLoan.getMonthlyPayment() + " For a total of "
						+ carLoan.getTotalPayment());
			}
			 //Mr. Wick Car nice so i buy
			//New cars with loan interest are a bad investment!
		else if (age == 45 && cash > 50_000) {
				double newCarPrice = 100_000;
				double downPayment = newCarPrice * 0.15;
				double interestRate = 0.05;
				int repaymentYears = 5;

				Loan carLoan = new Loan("Car Loan", (newCarPrice - downPayment), interestRate, repaymentYears);
				loans.add(carLoan);
				System.out.println("Monthly car Payment: " + carLoan.getMonthlyPayment() + " For a total of "
						+ carLoan.getTotalPayment());
			}
			// My houze pretty cooll
			if (age == 34 && cash > 200_000) {
				double newHousePrice = 350_000;
				double downPayment = 150_000;

				double interestRate = 0.05;
				double payment = 2_000;

				loans.add(new Loan("House Loan", (newHousePrice - downPayment), interestRate, payment, age,
						numberOfYears));
			}

			// -----=====88888=====-----
			// Loans
			// -----=====88888=====-----
			// Monthly loan payments
			for (Loan loan : loans) {
				for (int month = 0; month < 12; month++) {
					if (loan.getBalance() > 0 && loan.differed == false) {
						cash -= loan.makePayment();
					}
				}
			}


			// Bucket List
			// Go to the great wall of china and the forbidden city (more social credit)
			if (age == 37 && cash > 20_000) {
		    double chinaTrip = 5_000;
		    double payment = 0;
		    payment += chinaTrip; 

			cash -= payment;
			}
			if (age == 40 && cash > 30_000) {
				double russiaTrip = 10_00;
				double payment = 0;
				payment += russiaTrip;

				cash -= payment;
			}






//Calculate Debt Balance
			double debt = 0;
			for (Loan loan : loans)
				debt += loan.principal;

			// Output year-end review
			System.out.println("Balance at age: " + age + " is: " + cash + " with a debt of " + debt + " and "
					+ invested + " invested.");

			// Did you make it?
			if (age > 30 && cash < 0) {
				System.out.println("Out of cash. Q bozo!");
			}

			if (age > 79 && cash > 0) {
				System.out.println("Extraction Completed");
				break;
			}

		}
	}
} 