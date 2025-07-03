package csi.quiros.inheritance;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Point;

import javax.swing.ImageIcon;
import javax.swing.JPanel;


public class Dog extends JPanel{
	 
	
	
	
	
	int size;
	boolean wild = true;
	String hair;
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
	
		this.icon = new ImageIcon(new ImageIcon(getClass().getResource(directory)).getImage().getScaledInstance(100, 75,  java.awt.Image.SCALE_SMOOTH));

	}
	
	public void piss() {
		
		if(gender == true) {
			System.out.println("raise your leg");
		}
		System.out.println("phsssss");
		
	}
	
	public void die() {
		
	}
	
	public void wagTail() {
		
	}
	
	
	public class Shit {

		boolean hard;
		int size;
		String shape;
		
		
		public Shit() {

		}
		
		public Shit(boolean hard, int size, String shape) {
			super();
			this.hard = hard;
			this.size = size;
			this.shape = shape;
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
	
	public class Food {
		ImageIcon icon;
		String flavor;
		String color;
		boolean humanFood;
		Point point;
		
		
		public Food(String flavor, String color, boolean humanFood, String directory) {
			super();
			this.icon = new ImageIcon(new ImageIcon(getClass().getResource(directory)).getImage().getScaledInstance(50, 50,  java.awt.Image.SCALE_SMOOTH));
			this.flavor = flavor;
			this.color = color;
			this.humanFood = humanFood;
			
		}
		
		public Food(Point p) {
			this("Shrimp","Brown",false, "DogFood.png");
			this.point = p;
			
		}

		
		
		public Shit digest() {
			
			return new Shit();
		}
	}
	
	
	public Shit eat(Food f) {
		
		return f.digest();
	}
	
	
	public Noise bark() {
		return new Noise();
	}
	
	public void mate(Dog d) {
		
	
}
}