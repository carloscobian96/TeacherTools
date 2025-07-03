package csi.lopez.life1;

public class Loan {
	
	String name;
	
	double principal;
//	double balance;
	double annualInterestRate;
    double loanAmount;
    double paid;
    
    boolean differed = false;
	
	int numberOfYears;
	
	public Loan(String name, double principal, double annualInterestRate, int numberOfYears) {
		super();
		this.name = name;
		this.principal = principal;
		this.annualInterestRate = annualInterestRate;
		
		this.numberOfYears = numberOfYears;
		
	}
	

	public double makePayment() {
		
		
		
//		if(balance <0) {
//			double actualPayment = getMonthlyPayment() + balance;
//			balance = 0;
//			return actualPayment;
//		}
		if(getBalance() < getMonthlyPayment()) {
			double due = getBalance();
			paid+= due;
			return due;
		}else {
			paid+= getMonthlyPayment();
			return getMonthlyPayment();
		}
	}
	
	public double getBalance() {
		return( getTotalPayment() - paid);
	}
	
	
    //FInd the monthly pay 
    public double getMonthlyPayment() {
        double monthlyInterestRate = annualInterestRate / 1200;
        double monthlyPayment = principal * monthlyInterestRate / (1 - 1 / Math.pow
                (1 + monthlyInterestRate, numberOfYears * 12));
        return monthlyPayment;
    }

    //Find total payment
    public double getTotalPayment() {
    	return ( getMonthlyPayment() * numberOfYears * 12);
        
    }

    
	
	

}
