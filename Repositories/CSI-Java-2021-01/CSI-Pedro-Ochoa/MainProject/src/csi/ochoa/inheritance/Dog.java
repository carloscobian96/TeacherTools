package csi.ochoa.inheritance;

import javax.swing.ImageIcon;

public class Dog {

		
		String hair;
		int size; 
		boolean wild = true;
		boolean gender;
		ImageIcon icon;
		
		

		public Dog() {
			
			
		}  
		public Dog(String hair, int size, boolean wild, boolean gender, String directory) {
			super();
			this.hair = hair;
			this.size = size;
			this.wild = wild;
			this.gender = gender;
			this.icon = new ImageIcon(new ImageIcon(getClass().getResource(directory)).getImage().getScaledInstance(100, 100,  java.awt.Image.SCALE_SMOOTH));
		}


		public void piss() {
			
			System.out.println("tssss");{
				if(gender = true) {
					System.out.println("Raise leg");
				}
				System.out.println("tsssss");
			}	
		}
		
		public void die() {
			
		}
		
		public void wagTail() {
			
		}
		
		public void grow() {
			
			
		}
		
		
		public class Shit {

	
			ImageIcon icon;
			int shit_x;
			int shit_y;
			
			
			public Shit(int shit_x, int shit_y) {

				this.icon = new ImageIcon(new ImageIcon(getClass().getResource("Shit.jpeg")).getImage().getScaledInstance(100, 100,  java.awt.Image.SCALE_SMOOTH));
				this.shit_x = shit_x;
				this.shit_y = shit_y;	
				
			}
			
			
										
		}
		
		public void mate(Dog D) {
			
			
			
		}
		public void digest() {
			
		
			
			
			return;
		}
		
		

		public class Noise {
			public Noise(int i, boolean b) {
				
			}
			int decibels = 0;
			boolean recurring = false;
		}
	
		
		public class Food {
			public Food(String flavor, String color, boolean humanFood) {
				
			}
			
			
			ImageIcon icon;
			 int food_x;
			 int food_y;
			
			
			public Food (int food_y, int food_x) {
				this.icon = new ImageIcon(new ImageIcon(getClass().getResource("dogfood.jpeg")).getImage().getScaledInstance(100, 100,  java.awt.Image.SCALE_SMOOTH));
				this.food_x = food_x;
				this.food_y = food_y;
			
		}
		
			public class Piss {

				
				ImageIcon icon;
				int piss_x;
				int piss_y;
				
				
				public Piss(int piss_x, int piss_y) {

					this.icon = new ImageIcon(new ImageIcon(getClass().getResource("piss.jpeg")).getImage().getScaledInstance(100, 100,  java.awt.Image.SCALE_SMOOTH));
					this.piss_x = piss_x;
					this.piss_y = piss_y;	
		
		
				}
		
	
		public Noise bark(Noise n) {
			
			
			return new Noise(n.decibels, n.recurring);
		}

		}

		public Noise bark(Noise n) {
			// TODO Auto-generated method stub
			return null;
		}
}
	


