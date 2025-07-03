package csi.negron.Life;

public class Loans {
	public boolean differed = false;
	String name;
	double principal;
	double paymentAmount;
	private double annualInterestRate;
	int numberOfYears;
	    double loanAmount;
	    int remainingYears;
	    int getMonthlyPayment;
	    int getTotalPayment;
	     int paid;
	    private java.util.Date loanDate;

	    //Default Constructor
	    public Loans(String string, double d, double interestRate, int repaymentYears) {
	        this(2.5, 1, 1000);
	    }
	    //Return annualInterestRate
	    public double getAnnualInterestRate() {
	   
	   
	   
	        return annualInterestRate;
	    }
	  //Construct a loan specified annual interest rate
	    //number of years and loan amount
	    public Loans(double annualInterestRate, int numberOfYears, double loanAmount) {

	        this.annualInterestRate = annualInterestRate;
	        this.numberOfYears = numberOfYears;
	        this.loanAmount = loanAmount;

	        loanDate = new java.util.Date();
	    }
	int startAge;
	public Loans(String name, double balance, double rate, double paymentAmount, int startAge, int numberOfYears) {
	super();
	this.name = name;
	this.principal = balance;
	this.annualInterestRate = rate;
	this.paymentAmount = paymentAmount;
	this.startAge = startAge;
	this.numberOfYears = numberOfYears;
	// this.remainingYears = remainingYears;
	//this.balance = getTotalPayment;
	}
	public double makePayment() {
	principal += getMonthlyPayment();
	   return getMonthlyPayment();
	}
	double getMonthlyPayment() {
	// TODO Auto-generated method stub
	return 0;
	}
	public double getBalance() {
	return (getTotalPayment() - paid);
	}
	int getTotalPayment() {
	// TODO Auto-generated method stub
	return 0;
	}
	public void accureInterest (int frequency) {
	principal += principal*annualInterestRate;
	}
	public Object accureInterest() {
	// TODO Auto-generated method stub
	return null;
	}
	//Return numberOfYears
	    public int getNumberOfYears() {
	        return numberOfYears;
	    }
	    //Set a new numberOfYears
	    public void setNumberOfYears(int numberOfYears) {
	        this.numberOfYears = numberOfYears;
	    }

}
