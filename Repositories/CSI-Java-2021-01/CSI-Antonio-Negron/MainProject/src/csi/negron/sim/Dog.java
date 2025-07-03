package csi.negron.sim;

import java.awt.Point;

import javax.swing.ImageIcon;

public class Dog {

	String hair;
	int size;
	boolean wild = true;
	boolean gender = true;
	ImageIcon icon;
	 int shit_x;
	 int shit_y;
	 int food_x;
	 int food_y;
	
	
	
	Dog (){}
	public Dog(String hair, int size, boolean wild, boolean gender, String directory ) {
		super();
		this.hair = hair;
		this.size = size;
		this.wild = wild;
		this.gender = gender;
		this.icon = new ImageIcon(new ImageIcon(getClass().getResource(directory)).getImage().getScaledInstance(50, 50,  java.awt.Image.SCALE_SMOOTH));
	}

	public class Shit {
		boolean stink = true;
		int size;
		String consistency;
		ImageIcon icon = new ImageIcon(new ImageIcon(getClass().getResource("Dogshit.png")).getImage().getScaledInstance(50, 50,  java.awt.Image.SCALE_SMOOTH));
//		int shit_x;
//		 int shit_y;
		Point point;
		
		public Shit(boolean stink, int size, String consistency) {
			super();
			this.stink = stink;
			this.size = size;
			this.consistency = consistency;
		}
		public Shit() {
			super();
			this.size = 5;
			this.consistency = "Pasty";
			
		}
		
		public Point getLocation() {
			return point;
		}

		public void setLocation(Point location) {
			this.point = location;
		}
	}
	
	
	public class Food {
		boolean wet = false; 
		String taste;
		Point point;
		int bowlSize;
		ImageIcon icon = new ImageIcon(new ImageIcon(getClass().getResource("treat.png")).getImage().getScaledInstance(50, 50,  java.awt.Image.SCALE_SMOOTH));

//		public Shit digest() {
//			// TODO Auto-generated method stub
//			return null;
//		}
		public Food(boolean wet,String taste,int bowlSize) {
			super();
			this.wet=wet;
			this.taste=taste;
			this.bowlSize=bowlSize;
		}
		public Food(Point point) {
			super();
			this.taste="tasty";
			this.bowlSize=5;
			this.point=point;
		}
		
		public Shit digest() {
			
			return new Shit();
		}
		
	}
		public Shit eat(Food f) {
		
			return f.digest();
	}
	
	
    public class Noise{
    	int decibels;
    	boolean pitch;
    	
    	public Noise(int decibels, boolean pitch) {
			super();
			this.decibels = decibels;
			this.pitch = pitch;
		}
	}
    
    
	void piss() {
    	if (gender = true) {
    		System.out.println("Raise Leg");
    	}
    	System.out.println("Tsssss");
	}
	
	
	
	void die() {
		
	}
	
	void grow() {
		
	}
	
    Noise bark() {
    	return new Noise();
    }
    
    void wagTail() {
    	
    }
    
    public void Mate (Dog D) {
    	
    }
	
	
	
}


