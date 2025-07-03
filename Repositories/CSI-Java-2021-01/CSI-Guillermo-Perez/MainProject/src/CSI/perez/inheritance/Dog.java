package csi.perez.inheritance;

import java.awt.Point;

import javax.swing.ImageIcon;

public class Dog {
	String breed;
	String hair;
	int size;
	Boolean wild = true;
	Boolean gender;
	ImageIcon icon;

	public Dog(String breed, String hair, int size, Boolean wild, Boolean gender, String imageDir) {
		super();
		this.breed = breed;
		this.hair = hair;
		this.size = size;
		this.wild = wild;
		this.gender = gender;
		this.icon = new ImageIcon(new ImageIcon(getClass().getResource(imageDir)).getImage().getScaledInstance(120, 120,
				java.awt.Image.SCALE_SMOOTH));

	}
	public Dog() {

	}
	
	public void piss() {
		if (gender == true)
			;
		{
			System.out.println(" Raise leg, Tsssss");
		}
	}

	public void die() {

	}

	Noise bark() {
		return new Noise();
	}

	public void wagtail() {

	}

	public void mate(Dog D) {
	}
	public class Shit {
		int size;
		String color;
		String consistency;
	    ImageIcon icon;

		public Shit(int size, String color, String consistency) {
			super();
			this.size = size;
			this.color = color;
			this.consistency = consistency;
			this.icon = new ImageIcon(new ImageIcon(getClass().getResource("poop.png")).getImage().getScaledInstance(120, 120,
					java.awt.Image.SCALE_SMOOTH));
		}

		public Shit() {
			this(3,"Blue","Sharp");
		}

	}
	public class Food {
		Boolean healthy;
		String type;
		String texture;
		String color;
		ImageIcon icon;
		Point point;

		public Food(Boolean healthy, String type, String texture, String color) {
			super();
			this.healthy = healthy;
			this.type = type;
			this.texture = texture;
			this.color = color;
			this.icon = new ImageIcon(new ImageIcon(getClass().getResource("food.png")).getImage().getScaledInstance(120, 120,
					java.awt.Image.SCALE_SMOOTH));
		}
		
		public Food(Point point) {
			this.healthy = true;
			this.type = "Submarine";
			this.texture = "Rugged";
			this.color = "Green";
			this.icon = new ImageIcon(new ImageIcon(getClass().getResource("food.png")).getImage().getScaledInstance(60, 60,
					java.awt.Image.SCALE_SMOOTH));
			this.point = point;
			
		}
		 
		public Shit digest() {

			return new Shit();

		}
	}

	public Shit eat(Food f) {

		return f.digest();
	}



	public class Noise {
		String sound;
		int intention;
		Boolean loudness;
		
		
	
		
		public Noise(String sound, int intention, Boolean loudness) {
			super();
			this.sound = sound;
			this.intention = intention;
			this.loudness = loudness;
		}




		public Noise() {
		}



	}
}
