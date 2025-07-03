package csi.cobian.src;

public class TestBench {

	public static void main(String[] args) throws InterruptedException {

		double initial = 2000;
		double cash = 0;
		double debt = 0;
		double invested = 0;
		
		cash += initial;
		
		for (int i = 0; i <= 80; i++) { 
			
			// Formative Years
			if (i <= 17) {
				String location = "PR";
				double salary = 0;
				
				cash += salary;
				
			// 2 years at Iowa State
			} else if(i<=19) { 
				String location = "IA";
				double salary = 0;
				double tuition = 23_000 + 4_000 - 31_000; //Tuition + fees - scholarship
				double costOfLiving = 10_000; // Housing fees
				
				double loanInterest = 0.00;
				
				cash += salary;
				debt -= tuition;
				debt -= costOfLiving;
				debt += -((loanInterest *debt) * 12); // compounded monthly
					
			// Working as IT while studying bachelors at PUPR	
			} else if(i<=23) {
				String location = "PR";
				double salary = 10_000; // Part Time
				double tuition = 9_500 - 5_000; // tuition - Pell Grant 
				double food = 300 * 12;
				
				double investment =  1_000;
				double investmentInterest = 0.10;
				
				double debtPayment = 2000;
				double loanInterest = 0.00;
				
				cash += salary;
				cash -= food;
				cash -= tuition;
				
				debt += debtPayment;
				debt -= ((loanInterest * debt) * 12); // compounded monthly (Fix Formula)
				
				cash -= investment;
				invested += investment;// Invest at start of year.
				invested += invested * investmentInterest;
				
			}else if(i<=25) {
				// salary - 10% tax
				double salary = 40_000 * 0.9; 
				double rent = 12 * 1000;
				double food = 500 * 12;// 16$ daily food stipend
				// monthly gas expense + repairs + monthly car payment.  
				double gasAndCar = 30*24 + 400 + 0*12; 
				double monthlyExpenses = 400 * 12;
				
				double investment =  1_000;
				double investmentInterest = 0.25;
				
				double debtPayment = 5_000;
				double loanInterest = 0.049;
				
				cash += salary;
				cash -= food;
				cash -= rent;
				cash -= gasAndCar;
				cash -= monthlyExpenses;
				
				// Debt payment and interest calculation
				for(int month = 0; month < 12; month++) {
					debt += debt * loanInterest;
					
					cash -= debtPayment;
					debt += debtPayment; 
					
					// Repayment finished
					if(debt > 0) {
						cash += debt;
					}
				}
				
				cash -= investment;
				invested += investment;// Invest at start of year.
				invested += invested * investmentInterest;
				
			}else if(i<=27) {
				// Be a teacher at San Ignacio for a year, maybe 2
				double salary = 23_000 ; // salary, tax exempt 
				double rent = 12 * 1000;
				double food = 500 * 12;
				double gasAndCar = 30*12 + 400 + 0*12; 
				double monthlyExpenses = 300 * 12;
				
				double investmentInterest = 0.20;
				
				cash += salary;
				cash -= food;
				cash -= rent;
				cash -= gasAndCar;
				cash -= monthlyExpenses;
				
				// No aditions to investment portfolio
				invested += invested * investmentInterest;
				
			}else if(i<65) {
		        String location = "PR";

		        // salary - 10% tax
		        double salary = 50_000 * 0.9; 

		        // 2 bedroom apartment + electric/water/wi-fi bills
		        double rent = 12 * (1500 + 400);

		        // 30$ daily food stipend
		        double food = 30 * 365; 

		        // 60$ per month on gas.
		        // Approximately 1000$ a year on car reparations, tolls, licenses, oil and tire changes.
		        // Monthly car payment of 400$
		        double carAndExpenses = 60*12 + 1_000 + 400*12; 
		        
 				double investment =  5_000;
				double investmentInterest = 0.15;
				
		        cash += salary;
		        cash -= rent;
		        cash -= food;
		        cash -= carAndExpenses;
				
				
				invested += investment;// Invest at start of year.
				invested += invested * investmentInterest; //  compounded annually at end of year
			}else {
				//retired
				
				//Withdraw living expenses
				invested -= 25_000;
				cash += 25_000;
				
				//live
				cash -= 22_000;
				
			}
			
			
//			One-time purchase
			if(i==24) {
//				Buy a used car using cash.
				int usedCar = 5_000;
				cash -= usedCar;
			}
			
			System.out.println("Balance at age: " + i + " is: " + cash + " with a debt of " + debt + " and " + invested + " invested." );
		}

	}
	public void debtPayment(double ammount, double interest) {
		
	}
}