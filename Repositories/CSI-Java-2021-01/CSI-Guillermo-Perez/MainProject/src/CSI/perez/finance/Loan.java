/**
 * 
 */
package csi.perez.finance;

/**
 * @author guillermoperez
 *
 */
public class Loan {
	String name;
	double principal;
	double annualInterestRate;
	double numberOfYears;
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
		paid += getMonthlyPayment();
		return getMonthlyPayment();
	}

	public double getBalance() {
		return (getTotalPayment() - paid);
	}

//Find Monthly Payment
	public double getMonthlyPayment() {
		double monthlyInterestRate = annualInterestRate / 1200;
		double monthlyPayment = principal * monthlyInterestRate
				/ (1 - 1 / Math.pow(1 + monthlyInterestRate, numberOfYears * 12));
		return monthlyPayment;
	}

//Find total payment
	public double getTotalPayment() {
		double totalPayment = getMonthlyPayment() * numberOfYears * 12;
		return totalPayment;
	}
}