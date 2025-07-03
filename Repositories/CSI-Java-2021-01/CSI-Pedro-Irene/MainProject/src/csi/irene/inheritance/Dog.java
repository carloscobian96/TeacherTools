package csi.irene.inheritance;

import java.awt.Image;

import javax.swing.ImageIcon;
import javax.swing.JPanel;

public class Dog extends JPanel {

	String hair;
	int size;
	Boolean wild = true;
	boolean gender = true; // true = male
	ImageIcon icon;
	ImageIcon shit;
//	Constructors
	public Dog() {
		super();
	}

	public Dog(String hair, int size, Boolean wild, boolean gender, String directory) {
		super();
		this.hair = hair;
		this.size = size;
		this.wild = wild;
		this.gender = gender;
		this.icon = new ImageIcon((new ImageIcon(getClass().getResource(directory))).getImage().getScaledInstance(50, 50,  java.awt.Image.SCALE_SMOOTH));  // transform it back
	}
	
//	Methods
	public void piss() {
		if (gender == true) {
			System.out.println("Raise leg");
		}

		System.out.println("piss sounds");
	}

	public Shit eat(Food f) {

		return f.digest();
	}

	public void Die() {
	}
	
	public Noise Bark() {
		return new Noise();

	}

	public void Wagtail() {
		new Noise();
		System.out.println("wag wag");

		return;
	}

	public void Mate(Dog D) {
	}
	
	
// Internal Classes
	public class Shit {

		int size;
		boolean smelly;
		String color;
		public ImageIcon shit = new ImageIcon(new ImageIcon(getClass().getResource("Shit.jpg")).getImage().getScaledInstance(50, 50,  java.awt.Image.SCALE_SMOOTH));
		
		public Shit(boolean smelly, int size, String color) {
			super();
			this.size = size;
			this.smelly = smelly;
			this.color = color;
		}
	}

	public class Food {
		boolean moist;
		boolean musty;
		boolean bad;
		public ImageIcon icon = new ImageIcon(new ImageIcon(getClass().getResource("Food.png")).getImage().getScaledInstance(50, 50,  java.awt.Image.SCALE_SMOOTH));
	    public int food_x;
		public int food_y;

		
		public Food(boolean moist, boolean musty, boolean bad) {
			super();
			this.moist = moist;
			this.musty = musty;
			this.bad = bad;
		}
		
		public Food(int food_x, int food_y) {
			this(true,true,false);
			this.food_x = food_x;
			this.food_y = food_y;
		

		}
		public Shit digest() {

			return new Shit(bad, size, hair);
		}

	}

	public class Size {
		boolean loud;
		boolean annoying;

		public Size(boolean loud, boolean annoying) {
			super();
			this.loud = loud;
			this.annoying = annoying;
		}

	}


	public class Noise {
		int decibels;
		boolean recurring;
		
		public Noise() {			
		}

		public Noise(int decibels, boolean recurring) {
			super();
			this.decibels = decibels;
			this.recurring = recurring;
		}
	}	
}
