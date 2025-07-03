package csi.quiros.pkg;
import java.util.*;


public class PiedraPapelTijera {
	public static void main(String[] args) {
	String[] choices = {"Rock", "Paper", "Scissor"};
	Random r = new Random();
		
	String computerChoice = choices[r.nextInt(choices.length)];
	
	Scanner sc = new Scanner(System.in);
	System.out.print("Type an index: ");
	String userChoice = choices[sc.nextInt()];
	
	System.out.println("Computer chose: " + computerChoice);
	System.out.println("User chose: " + userChoice);
	
	if(computerChoice == userChoice) {
		System.out.println("It's a Tie!");
				}
	
	// Lose
	if(computerChoice == choices[1] && userChoice == choices[0]) {
		System.out.println("You Lose!");		
	}
	if(computerChoice == choices[0] && userChoice == choices[2]) {
		System.out.println("You Lose!");
	}
	if(computerChoice == choices[2] && userChoice == choices[1]) {
		System.out.println("You Lose!");
	}
	else if(computerChoice == choices[0] && userChoice == choices[1]) {
		System.out.println("You Win!");
	}
	else if(computerChoice == choices[1] && userChoice == choices[2]) {
		System.out.println("You Win!");
	}
	else if(computerChoice == choices[2] && userChoice == choices[0]) {
		System.out.println("You Win!");
	}
	
	
	
	}
}
