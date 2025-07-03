package csi.ochoa.pkg;

import java.util.*;

//import java.util.Random;

public class PiedraPapelTijera {

	public static void main(String[] args) {
	
		
		String[] choices = {"Rock","Paper","Scissor"};
		Random r = new Random();
		
		int randomInt = r.nextInt(choices.length);
		String computerChoice = choices[r.nextInt(choices.length)];
		
		Scanner sc = new Scanner(System.in);
		
		
		System.out.println("Type an index: ");
		int inputInt = Arrays.asList(choices).indexOf(sc.nextLine());
		String userChoice = choices[sc.nextInt()];
		
		System.out.println("Computer chose: " + computerChoice);
		System.out.println("User chose: " + userChoice);
		
		if(computerChoice == userChoice) {
			System.out.println("It's a Tie!");
		}
		else if(computerChoice == choices[0] && userChoice == choices[1]) {
			System.out.println("You Win!");
		}
		
		else if(computerChoice == choices [1] && userChoice == choices [0]) {
			
			System.out.println("You Lose!");
		}
		
		else if(computerChoice == choices [2] && userChoice == choices [1]) {
			
			System.out.println("You Lose!");
		}

		else if(computerChoice == choices[1] && userChoice == choices[2]) {
			System.out.println("You Win!");
			
		}
		
		else if(computerChoice == choices[0] && userChoice == choices[2]) {
			System.out.println("You Win!");
		}
		
		else if(computerChoice == choices[2] && userChoice == choices[0]) {
			System.out.println("You Lose!");
		}
		
		
		else {
			System.out.println("Something went wrong");
		}
		
		
		
//		String Rock;
//		String Paper;
//		String Scissor;
//		
//		Scanner sc = new Scanner(System.in);
//		System.out.println("Enter First Number");
//		int a = sc.nextInt();
//		System.out.println("Enter Second Number");
//		
//
//		
//		String[] arr = {"1","2","3","4","5"};
//		Random r = new Random();
//		int randomNumber = r.nextInt(arr.length);
//		System.out.println(arr[randomNumber]);
//	

	}
}
