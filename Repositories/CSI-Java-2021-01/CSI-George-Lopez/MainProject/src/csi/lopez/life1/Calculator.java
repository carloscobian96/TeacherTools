package csi.lopez.life1;


import java.util.*;

public class Calculator {

	public Calculator() {
		// TODO Auto-generated constructor stub
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int lifeExpectancy = 75;
		double startingAmount = 0;
		double cash = 0;
		
		Loan monthlyPayment;
		
		List<Loan> loans = new ArrayList<Loan>();
		
		loans.add(new Loan("Student Loans", 0, 0.0466, 30));
		loans.add(new Loan("Personal Loans", 0, 0.16, 10));
		loans.add(new Loan("Mortgage Loans", 0, 0.03125, 30));
		loans.add(new Loan("CreditCard", 0, 0.29, 1));

		cash += startingAmount;
		
		for(int age = 0; age <= lifeExpectancy; age++) {
			
			//Childhood 
			if(age < 18) {
				String location = "PR";
				double salary = 80;
			
				cash += salary; 
				
			// College desde 18 - 23, until i get bachelor
			} else if(age < 23) {
				String location = "GA";
				double salary = 0;
				
				double tuition = 31_000 + 4_000;
				double costOfLiving = 12_000;
				
//				double loanInterest = 0.049;
				
				cash += salary;
				
				loans.get(0).principal += costOfLiving;
				loans.get(0).principal += tuition;
				loans.get(0).differed = true;
				
				
			//Work
			} else if(age < 60) {					
					String location = "PR";
					double salary = 116_193* 0.9;
					
					double rent = 12 * (1500 + 400);
					double food = 30 * 365; 
					double carExpenses = 60*12 + 1_000 + 400*12; 
					
//					double costOfLiving = rent + food + carExpenses;
					 
			        cash += salary;
			        cash -= rent;
			        cash -= food;
			        cash -= carExpenses;
			        
					loans.get(0).differed = false;

				
			} else {
				// retired
				
				
			}
			
			//----------Additional Stuff----------
			
			
			
			//----Cars(not the movie)-------
			if(age == 24 && cash >= 15_000) {

				double usedCarPrice = 5_000.0;
				cash -= usedCarPrice;
				
			} else if( age == 24 && cash < 10_000) {
				
				//pickup trucks all the way
				double newCarPrice = 32_000;
				double downPayment = 5_000;
				
				loans.add(new Loan ("Car loan",
						(newCarPrice - downPayment),
						0.05,
						6));
				
			} if(age == 34 && cash >= 15_000) {

				double usedCarPrice = 5_000.0;
				cash -= usedCarPrice;
				
			} else if( age == 34 && cash < 10_000) {
				
				//Pickup trucks all the way
				double newCarPrice = 32_000;
				double downPayment = 5_000;
				
				loans.add(new Loan ("Car loan",
						(newCarPrice - downPayment),
						0.05,
						6));
				
			}if(age == 44 && cash >= 15_000) {

				double usedCarPrice = 5_000.0;
				cash -= usedCarPrice;
				
			} else if( age == 44 && cash < 10_000) {
				
				//Pickup trucks all the way
				double newCarPrice = 32_000;
				double downPayment = 5_000;
				
				
				loans.add(new Loan ("Car loan",
						(newCarPrice - downPayment),
						0.05,
						6));
				
			}if(age == 54 && cash >= 15_000) {

				double usedCarPrice = 5_000.0;
				cash -= usedCarPrice;
				
			} else if( age == 54 && cash < 10_000) {
				
				//Pickup trucks all the way
				double newCarPrice = 32_000;
				double downPayment = 5_000;
				
				loans.add(new Loan ("Car loan",
						(newCarPrice - downPayment),
						0.05,
						6));
			}
			
			
			
			// ----------BUY HOUSE-------------
			// Buy a House at 35
			if(age == 35 && cash >= 200_000){
			        double cashPrice = 200_000;
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
			
			
		
			
			
//			loans.stream().filter(o -> age >=o.startUp).map(o -> o.makePayment());
//			loans.stream().map(o -> o.accureInterest());
			
			
// --------------------------------------------------
			// COSAS DE LOANS 
// --------------------------------------------------
			
//			for(int month = 0; month < 12; month++) {
//				
//				loans.forEach(loan -> loan.makePayment());
//				loans.forEach(loan -> loan.accureInterest());
//				
//			}
			
			
			
			//Monthly Payment
			for(Loan loan: loans) {
				for(int month = 0; month < 12; month++) {
				    if(loan.getBalance() > 0 && loan.differed == false) {
				      cash -= loan.makePayment();	
//				      loan.accureInterest();
//				      loan.getMonthlyPayment();
				     
				    }
				  }
				}
			
			
			double debt = 0;
			for(Loan loan : loans) {
				debt += loan.getBalance();
			}
			
			System.out.println("Balance at age: " + age + " is: " + cash + " with a debt of " + debt );
			
			
			if(cash < 0) {
				  System.out.println("You're broke and your dead.");
				  break;
				}
			
		}
	}
}


