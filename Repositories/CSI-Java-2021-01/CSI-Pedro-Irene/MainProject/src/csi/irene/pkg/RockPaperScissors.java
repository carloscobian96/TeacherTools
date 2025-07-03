package csi.irene.pkg;
import java.util.*;
public class RockPaperScissors {
	public static void main(String[] args) {
	
	
	String[] choices= {"Rock", "Paper", "Scissors"};
	Random r=new Random();
	//int randomInt = r.nextInt(choices.length)
	String computerChoice = choices[r.nextInt(choices.length)];
	
	Scanner sc = new Scanner(System.in);
	
	//int inputInt = sc.nextInt();
	System.out.print("Type an index: ");
	String userChoice = choices[sc.nextInt()];
	
	System.out.println("Computer chose: " + computerChoice);
	System.out.println("User chose: " + userChoice);
	
	if(computerChoice == userChoice) {
		System.out.println("Its a Tie!");
	}
	else if(computerChoice == choices[0] && userChoice == choices[1]) {
//		Computer chose Rock and user chose Paper
		System.out.println("You Win!");


	}
	
	else {
		System.out.println("Something went wrong!");
	}
	
	 if (computerChoice == choices[0] && userChoice == choices[2]) {
	System.out.println("You Lose!");
	
	}
	
	 else if(computerChoice == choices[1] && userChoice == choices[0]) {
	System.out.println("You lose!");
	 }
	if(computerChoice == choices[1] && userChoice == choices[2]) {
	System.out.println("You Win!");
	}
	else if(computerChoice == choices[2] && userChoice == choices[0]) {
		System.out.println("You retar!");
	}
	if(computerChoice == choices[2] && userChoice == choices[1]) {
	System.out.println("Very Good");	
	}
	}
}
