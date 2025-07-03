package csi.lopez.sim;

import java.awt.*;
import java.io.File;
import java.io.IOException;

import javax.print.attribute.standard.Media;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.sound.sampled.LineUnavailableException;
import javax.sound.sampled.UnsupportedAudioFileException;
import javax.swing.ImageIcon;
import javax.swing.JPanel;


//Java program to play an Audio
//file using Clip Object
import java.io.File;
import java.io.IOException;
import java.util.Scanner;

import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.sound.sampled.LineUnavailableException;
import javax.sound.sampled.UnsupportedAudioFileException;


public class Dog extends JPanel{
	
	
	
	
	
	int size; //ma x weight
	boolean wild = true;
	String hair;
	boolean female; //male = true
	ImageIcon icon;
	
	
	public Dog() {
		// TODO Auto-generated constructor stub
//		initDog();
	}
	
//	private void initDog() {
//
////        addKeyListener(new TAdapter());
//        setBackground(new Color(50, 150, 150));
//        setFocusable(true);
//
//        setPreferredSize(new Dimension(B_WIDTH, B_HEIGHT));
//        
//	}
	
	public Dog(String hair, int size, boolean wild, boolean female, String directory) {
		super();
		this.hair = hair;
		this.size = size;
		this.wild = wild;
		this.female = female;
		this.icon = new ImageIcon(new ImageIcon(getClass().getResource(directory)).getImage().getScaledInstance(50, 50,  java.awt.Image.SCALE_SMOOTH));
	}
	
	public class Piss{
		
	

	
		Point location;
		ImageIcon icon;
		
		
		public Piss() {
			this.icon = new ImageIcon(new ImageIcon(getClass().getResource("piss.png")).getImage().getScaledInstance(50, 50,  java.awt.Image.SCALE_SMOOTH));
		}
		
		public Point getLocation() {
			return location;
		}

		public void setLocation(Point location) {
			this.location = location;
		}
		
		public Piss piss() {
			
			return new Piss();
		}
	}
	
	
	
	public void die() {
		
	}
	
	public void wagTail() {
		
	}
	
	
	public class Shit {

		boolean hard;
		int size;
		String shape;
		ImageIcon icon;
		Point location;
		
		
		public Shit() {
			super();
			this.hard = true;
			this.size = 40;
			this.shape = "long";
			this.icon = new ImageIcon(new ImageIcon(getClass().getResource("shit.png")).getImage().getScaledInstance(50, 50,  java.awt.Image.SCALE_SMOOTH));
			

		}
		
//		public Shit(Point location) {
//			super();
//			this.location = location;
//		}
		

		public Shit(boolean hard, int size, String shape) {
			super();
			this.hard = hard;
			this.size = size;
			this.shape = shape;
			 
		}

		public Point getLocation() {
			return location;
		}

		public void setLocation(Point location) {
			this.location = location;
		}


	}
	
	public class Noise {
		int decibels;
		boolean recurring;
		Clip clip;
		AudioInputStream audioInputStream;
	    String filePath = "german-shephard-bark.mp3";
	    
		public Noise() {
//			try {
//				AudioInputStream audioInput = AudioSystem.getAudioInputStream(getClass().getResource("german-shephard-bark.mp3"));
//				this.clip = AudioSystem.getClip();
//				clip.open(audioInput);
////				clip.start();
//			} catch (UnsupportedAudioFileException | IOException | LineUnavailableException e) {
//				// TODO Auto-generated catch block
//				e.printStackTrace();
//			}
//			
//			String bip = "bip.wav";
//			Media hit = new Media(new File(bip).toURI().toString());
//			MediaPlayer mediaPlayer = new MediaPlayer(hit);
//			mediaPlayer.play();
	
//			 try {
//				// create AudioInputStream object
//				audioInputStream = AudioSystem.getAudioInputStream(new File(filePath).getAbsoluteFile());
//
//				// create clip reference
//				clip = AudioSystem.getClip();
//				  
//				// open audioInputStream to the clip
//				clip.open(audioInputStream);
//			} catch (UnsupportedAudioFileException | IOException | LineUnavailableException e) {
//				// TODO Auto-generated catch block
//				e.printStackTrace();
//			}
		}


		public Noise(int decibels, boolean recurring) {
			super();
			this.decibels = decibels;
			this.recurring = recurring;
		}
		
		
		
	}
	
	public class Food {
		public Food(String flavor, String color, boolean humanFood) {
			
		}
		public Food() {
			// TODO Auto-generated constructor stub
		}
		String flavor;
		String color;
		boolean humanFood;
		
		public Shit digest() {
			
			return new Shit();
		}
	}
	
	
	public Shit eat(Food f) {
		
		return f.digest();
	}
	
//	public Noise bark(Noise n) {
//		
//		return new Noise(n.decibels, n.recurring);
//	}
	
	public Noise bark() {
		
		Noise n = new Noise();
		n.clip.start();
		return n;
	}
	
	public void mate(Dog d) {
		
	}
	
	public void grow() {
		
	}

}
