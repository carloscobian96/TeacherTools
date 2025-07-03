/**
 * 
 */
package csi.cobian.src;

import java.util.*;

/**
 * @author carlos.cobian
 *
 */
public class RockPaperScissors {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		
		String[] choices = {"Rock", "Paper", "Scissors"};
		Random r = new Random();    
		
//		int randomInt = r.nextInt(choices.length)
		String computerChoice = choices[r.nextInt(choices.length)];
		
		Scanner sc = new Scanner(System.in);


		System.out.print("Type your choice: ");
		int inputInt = Arrays.asList(choices).indexOf(sc.nextLine());
		String userChoice = choices[inputInt];

		System.out.println("Computer chose: " + computerChoice);
		System.out.println("User chose: " + userChoice);

		if(computerChoice == userChoice) {
			System.out.println("It's a Tie!");
		}
		else if(computerChoice == choices[0] && userChoice == choices[1]) {
//			Computer chose Rock and user chose Paper
			System.out.println("You Win!");
		}
		//Other else if
		
//		Finally
		else {
			System.out.println("Something went wrong!");
		}
	}

}
