package csi.negron.pkg;


	import java.util.*;
	import java.util.Scanner;

	public class RockPaperScissors {
	  public static void main(String[] args) {  
		  Random r=new Random();
	   String[]choices= {"Rock","Paper","Scissor"};
	   String computerChoice=choices[r.nextInt(choices.length)];
	   Scanner sc=new Scanner(System.in);
	   
	
	   
	   System.out.println("Type your choice:");
	   int inputInt=Arrays.asList(choices).indexOf(sc.nextLine());
	   String userChoice=choices[inputInt];
	   
	   System.out.println("Computer chose"+ computerChoice);
	   System.out.println("User Chose"+userChoice);
	   
	   if(computerChoice==userChoice) {
		   System.out.println("Its a Tie!");
	   }
	   else if(computerChoice==choices[0]&& userChoice==choices[1]) {
		   System.out.println("You Win!");
	   }
	   else if(computerChoice==choices[1]&& userChoice==choices[0]) {
		   System.out.println("You Lost!");
	   }
	   else if(computerChoice==choices[0]&& userChoice==choices[2]) {
		   System.out.println("You Lost!");
	   }
	   else if(computerChoice==choices[2]&& userChoice==choices[0]) {
		   System.out.println("You Win!");
	   }
	   else if(computerChoice==choices[1]&& userChoice==choices[2]) {
		   System.out.println("You Win!");
	   }
	   else if(computerChoice==choices[2]&& userChoice==choices[1]) {
		   System.out.println("You Lost!");
	   }
	   else {
		   System.out.println("Something Went Wrong");
	   }
	  } 
	}
	

	