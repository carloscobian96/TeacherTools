package csi.lopez.pkg;

import java.util.Random;
import java.util.*;

public class RockPaperScissor {

	public RockPaperScissor() {
		// TODO Auto-generated constructor stub
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int i = 0;
		
		while(true) {
			String[] choices = {"Rock", "Paper", "Scissor"};
			Random r = new Random();
			
			String computerChoice= choices[r.nextInt(choices.length)];
//			System.out.println(arr[randomChoice]);
			
			
			Scanner sc= new Scanner(System.in);
			
			
			String userChoice=null;
			try {
				System.out.print("Type your choice:  ");
				int inputInt = Arrays.asList(choices).indexOf(sc.nextLine());
				userChoice = choices[inputInt];
			} catch (Exception e) {
				// TODO Auto-generated catch block
//				e.printStackTrace();
				System.out.println("Something's wrong");
				System.exit(0);
			}
			
			
			System.out.println("Computer Chose: " + computerChoice);
			System.out.println("You Chose: "+ userChoice);
			
			//You Chose Paper
			if(userChoice == choices[1] && computerChoice == choices[0]) {
				System.out.println("You Win!");	
			} 
			
			else if(userChoice == choices[1] && computerChoice == choices[2]) {
				System.out.println("You Lose!");	
			} 
			
			//You Chose Rock
			else if(userChoice == choices[0] && computerChoice == choices[1]) {
				System.out.println("You Lose!");	
			} 
			else if(userChoice == choices[0] && computerChoice == choices[2]) {
				System.out.println("You Win!");	
			} 
			
			//You Chose Scissor
			else if(userChoice == choices[2] && computerChoice == choices[0]) {
				System.out.println("You Lose!");	
			} 
			else if(userChoice == choices[2] && computerChoice == choices[1]) {
				System.out.println("You Win!");	
			} 
			
			
			//Tied 
			else if(computerChoice == userChoice) {
				System.out.println("You Tied!");
			}
			else {
				System.out.println("Something went wrong");
			}
			
			i++;
		}
		
		
		
		
		
		
		
		
//		if(PlayerWin == true) {
//			System.out.println("You Win!");
//		} else if(PlayerWin == false) {
//			System.out.println("You Lose!");
//		}
	}

}
