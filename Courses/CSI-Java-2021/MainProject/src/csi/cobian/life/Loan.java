package csi.cobian.life;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.text.DecimalFormat;

public class Loan {

	String name;
	double principal;
	double annualInterestRate;
	int numberOfYears;
//	private static final DecimalFormat df = new DecimalFormat("#.##");


	double paid;
	boolean differed = false;
	
	public Loan(String name, double principal, double annualInterestRate, int numberOfYears) {
		super();
		this.name = name;
		this.principal = principal;
		this.annualInterestRate = annualInterestRate;
		this.numberOfYears = numberOfYears;
	}
	
	public double makePayment() {
		
		if(getBalance() < getMonthlyPayment()) {
			double due = getBalance();
			paid += due;
			return due;
		}else {
			paid += getMonthlyPayment();
			return getMonthlyPayment();	
		}
	}
	
	public double getBalance() {
		return ( getTotalPayment() - paid );
	}
	
    //Find monthly payment
    public double getMonthlyPayment() {
        double monthlyInterestRate = annualInterestRate / 1200;
        double monthlyPayment = principal * monthlyInterestRate / (1 - 1 / Math.pow
                (1 + monthlyInterestRate, numberOfYears * 12));
		
//		double rounded = new BigDecimal(monthlyPayment).setScale(2, RoundingMode.HALF_UP).doubleValue();
		return monthlyPayment;
    }

    //Find total payment
    public double getTotalPayment() {
        return (getMonthlyPayment() * numberOfYears * 12 );
    }
	
}





//if(balance < 0) {
//double actualPayment = getMonthlyPayment() + balance;
//balance = 0;
//return actualPayment;
//}
