package csi.ochoa.inheritance;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.FontMetrics;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import javax.swing.ImageIcon;
import javax.swing.JPanel;
import javax.swing.Timer;

import csi.ochoa.inheritance.Dog.Shit;


public class DogPound extends JPanel implements ActionListener {

	List<Dog> dogs = new ArrayList<Dog>();
	List<Dog.Food> food = new ArrayList<Dog.Food>();
	List<Dog.Shit> shit = new ArrayList<Dog.Shit>();
	List<Dog.Piss> piss = new ArrayList<Dog.Piss>();

	private int B_WIDTH = 800;
	private int B_HEIGHT = 800;
	private final int ALL_DOGS = 50;
	private final int DELAY = 140;

	private final int x[] = new int[ALL_DOGS];
	private final int y[] = new int[ALL_DOGS];

	private boolean leftDirection = false;
	private boolean rightDirection = true;
	private boolean upDirection = false;
	private boolean downDirection = false;
	private boolean isRunning = true;

	private Timer timer;
	

	

	public DogPound() {

		

		initDogPound();
	}

	private void initDogPound() {
		dogs.add(new Terrier());

        addKeyListener(new TAdapter());
		
		setBackground(new Color(127, 37, 97));
		setFocusable(true);

		setPreferredSize(new Dimension(B_WIDTH, B_HEIGHT));

		timer = new Timer(DELAY, this);
		timer.start();

	}


	@Override
	public void paintComponent(Graphics g) {
		super.paintComponent(g);


		doDrawing(g);
	}

	private void doDrawing(Graphics g) {
		

			for (int z = 0; z < dogs.size(); z++) {

					g.drawImage(dogs.get(z).icon.getImage(), x[z], y[z], this);

			}
			Toolkit.getDefaultToolkit().sync();
		

			for (int z = 0; z < food.size(); z++) {

					g.drawImage(food.get(z).icon.getImage(), food.get(z).food_x, food.get(z).food_y, this);

			}
			Toolkit.getDefaultToolkit().sync();
			
			for (int z = 0; z < shit.size(); z++) {

				g.drawImage(shit.get(z).icon.getImage(), shit.get(z).shit_x, shit.get(z).shit_y, this);

		}
		Toolkit.getDefaultToolkit().sync();
		

	}
	
	private void checkFood() {
		
		Random rd = new Random();
		
		if(food.size() < 3) {
			
		food.add(new Dog().new Food(rd.nextInt(500),rd.nextInt(500)));
			
		}
		
		   
		   for(Dog.Food f : food) {
	    		
	    		if ((x[0] == f.food_x) && (y[0] == f.food_y)) {
	            	
	    			
	            	
	            }
	    	}
	        
	   }
	
	
private void checkShit() {
		
		Random rd = new Random();
		
		if(shit.size() < 1) {
			
		shit.add(new Dog().new Shit(rd.nextInt(500),rd.nextInt(500)));
			
		}
		
		   
		   for(Dog.Shit s : shit) {
	    		
	    		if ((x[0] == s.shit_x) && (y[0] == s.shit_y)) {
	            	
	    			
	            	
	            }
	    	}
	        
	   }
	
	@Override
	public void actionPerformed(ActionEvent e) {
		
	if (isRunning) {
		move();
        checkCollision();
        checkFood();
        checkShit();

	}
	
	repaint();
	
	}

	 private void checkCollision() {

			for (int z = dogs.size(); z > 0; z--) {

	    	    if ((z > 4) && (x[0] == x[z]) && (y[0] == y[z])) {
	    	        isRunning = false;
	    	    }
	    	}
			Random rd = new Random();

			if (y[0] >= B_HEIGHT) {

	        	upDirection = rd.nextBoolean();
                rightDirection = rd.nextBoolean();
                leftDirection = rd.nextBoolean();
                downDirection = false;
	        }

	        if (y[0] < 0) {

	        	leftDirection = rd.nextBoolean();
                upDirection = false;
                downDirection = rd.nextBoolean();
                rightDirection = rd.nextBoolean();
	        }

	        if (x[0] >= B_WIDTH) {

	        	upDirection = rd.nextBoolean();
                rightDirection = false;
                leftDirection = rd.nextBoolean();
                downDirection = rd.nextBoolean();
	        }
	        
	        if (x[0] < 0) {
	           
	        	leftDirection = false;
                upDirection = rd.nextBoolean();
                downDirection = rd.nextBoolean();
                rightDirection = rd.nextBoolean();
	        }
	       
	    }
	
	private class TAdapter extends KeyAdapter {

		@Override
		public void keyPressed(KeyEvent e) {


		}
	}
	

	
	 private void move() {

	        for (int z = dogs.size(); z > 0; z--) {
	            x[z] = x[(z - 1)];
	            y[z] = y[(z - 1)];
	        }

	        if (leftDirection) {
	            x[0] -= ALL_DOGS;
	        }

	        if (rightDirection) {
	            x[0] += ALL_DOGS;
	        }

	        if (upDirection) {
	            y[0] -= ALL_DOGS;
	        }

	        if (downDirection) {
	            y[0] += ALL_DOGS;
	        }
	        
	        
	   	 Random rd = new Random(); 

	     if(rd.nextInt(5) == 3) {
			leftDirection = rd.nextBoolean();
			upDirection = rd.nextBoolean();
			downDirection = rd.nextBoolean();
			rightDirection = rd.nextBoolean();
			
			}
	        
	        
	        
	        
	    }
	 

	
	
	
}



