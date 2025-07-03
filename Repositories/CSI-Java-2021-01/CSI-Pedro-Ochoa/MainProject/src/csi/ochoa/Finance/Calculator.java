package csi.ochoa.Finance;

import java.util.*;

public class Calculator {

	public static void main(String[] args) throws InterruptedException {

		double initial = 3000;
		double cash = initial;
		double invested = 0;

		List<Loan> loans = new ArrayList<Loan>();

		loans.add(new Loan("Student Loans", 0, 0.0465, 30));
		loans.add(new Loan("Personal Loans", 0, 0.016, 10));
		loans.add(new Loan("Mortgage Loans", 0, 0.03125, 30));
		loans.add(new Loan("CreditCard", 0, 0.29, 99));

		cash += initial;

		for (int age = 0; age <= 80; age++) {

			if (age < 17) { // highschool

				String location = "PR";
				double salary = 0;

				cash += salary;

			} else if (age < 19) { //// florida University of Miami

				String location = "FL";
				double salary = 23_000;
				double tuition = 50_000 + 5_000 - 40_000;
				double costOfLiving = 7_500;
				double Investment = 5_000;
				
				cash += Investment;
				cash += salary;
				loans.get(0).principal += costOfLiving;
				loans.get(0).principal += tuition;
				loans.get(0).differed = true;

			} else if (age < 23) { // college

				String location = "FL";
				double salary = 10_000;
				double tuition = 50_000;
				double costOfLiving = 8_000;
				double Investment = 5_000;

				double food = 600 * 12;

				cash += salary;

				loans.get(0).principal += tuition;
				loans.get(0).principal += food;
				loans.get(0).principal += costOfLiving;
				loans.get(0).differed = true;

			} else if (age < 28) { // work

				String location = "FL";
				double salary = 60_000 * 0.9;
				double costOfLiving = 20_000;
				double food = 1000 * 12;
				double Investment = 7_500;
//				double carAndExpenses = 100 * 12 + 3_000 + 800 * 12;


				cash += salary;

				cash += Investment;
				cash -= food;
				cash -= costOfLiving;
//				loans.get(0).balance += carAndExpenses;
				loans.get(0).differed = false;
				
				
				
				
			} else if (age < 40) { // work

				String location = "FL";
				double salary = 80_000 * 0.9;
				double costOfLiving = 20_000;
				double food = 1000 * 12;
////				double carAndExpenses = 100 * 12 + 3_000 + 800 * 12;
				double rent = 12 * (1500 + 400);
				double Investment = 10_000;

				cash += salary;

				cash += Investment;
				cash -= rent;
				cash -= food;
				cash -= costOfLiving;
			
				loans.get(0).differed = false;
			} else if (age < 65) { // retire
				// salary - 10% tax
				double salary = 200_000 * 0.9;

				// 2 bedroom apartment + electric/water/wi-fi bills
				double rent = 12 * (1500 + 400);

				// 30$ daily food stipend
				double food = 60 * 365;
				double costOfLiving = 20_000;
				double interestRate = 0.05;
				double payment = 230;

				cash += salary;
				cash += rent;
				cash += food;
				cash += costOfLiving;
//				cash -= carAndExpenses;

			} else if (age < 80) {// be with the family

			}
			
			
			// sdfdsf
			for (Loan loan : loans) {

				for (int month = 0; month < 12; month++) {
					if (loan.getBalance() > 0 && loan.differed == false) {
						cash -= loan.makePayment();
					}
				}
			}

			double debt = 0;
			for (Loan loan : loans) {

				debt += loan.getBalance();
			}


			if (age == 30) {

				double newCarPrice = 40_000;
				double downPayment = 5_000;
				int repaymentYears = 10;
				cash -= newCarPrice;
			}

			if (age == 40) {

				double housecost = 200_000;
				double downPayment = 200_000;
				
				cash -= housecost;
			}

			if (age == 47) {

				double newCarPrice = 23_000;
				double downPayment = 23_000;
				int repaymentYears = 0;
				
				cash -= newCarPrice;

				
			}
	

			System.out.println("Balance at age: " + age + " is: " + cash + " with a debt of " + debt + " and "
					+ invested + " invested.");

			if (cash < 0) {
				System.out.println("you broke, die");
				break;
			}
		}

	}
}
