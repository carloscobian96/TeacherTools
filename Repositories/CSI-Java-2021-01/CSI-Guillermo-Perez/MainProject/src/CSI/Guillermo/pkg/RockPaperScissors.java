/**
 * 
 */
package csi.guillermo.pkg;

import java.util.Random;
import java.util.Scanner;

/**
 * @author guillermoperez
 *
 */
public class RockPaperScissors {
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String[]choices = {"rock", "paper", "scissor"};
		Random r = new Random();
		
		String computerChoice = choices[r.nextInt(choices.length)];
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Type an index: ");
		String userChoice = choices[sc.nextInt()];
		
		System.out.println("Computer chose: " + computerChoice);
		System.out.println("User chose: " + userChoice);
		
		if(computerChoice == userChoice) {
			System.out.println("Its a Tie🙀");
			}
		
		else if(computerChoice == choices[0] && userChoice == choices[1]) {
			System.out.println("You win🥳");
			}
		else if(computerChoice == choices[0] && userChoice == choices[2]) {
			System.out.println("You loose😢");
			}
		else if(computerChoice == choices[1] && userChoice == choices[0]) {
			System.out.println("you loose😢");	
		}
		else if(computerChoice == choices[1] && userChoice == choices[2]) {
			System.out.println("You win🥳");
		}
		else if(computerChoice == choices[2] && userChoice == choices[0]) {
		System.out.println("You win🥳");
	    }
		else if(computerChoice == choices[2] && userChoice == choices[1]) {
		System.out.println("You loose😢");
		}
		}
	
		
	
	    
	
}

