package csi.negron.sim;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.FontMetrics;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.Point;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import javax.swing.Timer;

import csi.negron.sim.Dog.Food;
import csi.negron.sim.Dog.Shit;

import javax.swing.ImageIcon;
import javax.swing.JPanel;

public class DogPound extends JPanel implements ActionListener {
	private Image background;

	List<Dog> dogs1 = new ArrayList<Dog>();
	List<Dog.Shit> dogshit = new ArrayList<Dog.Shit>();
	List<Dog.Food> food = new ArrayList<Dog.Food>();
	private int B_WIDTH = 1000;
	private int B_HEIGHT = 1000;
	private int DOG_SIZE = 10;
	private int ALL_DOGS = 120;
	private int shit_x;
	private int shit_y;
	private int food_x;
	private int food_y;
	private int shitScore = 0;
	private final int RAND_POS = 10;
	private boolean inGame = true;

	private final int x[] = new int[ALL_DOGS];
	private final int y[] = new int[ALL_DOGS];

	private int Dogs;
	

	private boolean leftDirection = false;
	private boolean rightDirection = true;
	private boolean upDirection = false;
	private boolean downDirection = false;
	private boolean isRunning = true;

	private Timer timer;
	private final int DELAY = 140;
	//public ImageIcon dogfood = new ImageIcon(new ImageIcon(getClass().getResource("treat.png")).getImage().getScaledInstance(50, 50,  java.awt.Image.SCALE_SMOOTH));

	private int count;

	public DogPound() {
		dogs1.add(new AmericanBully());
		initBoard();
	}

	private void initBoard() {


		setBackground(new Color(50, 150, 150));
		setFocusable(true);
		setPreferredSize(new Dimension(B_WIDTH, B_HEIGHT));
		initSimulation();
	}

	private void initSimulation() {

		Dogs = 1;

		for (int z = 0; z < Dogs; z++) {
			x[z] = 50 - z * 10;
			y[z] = 50;
		 }
		locateFood();
		
		timer = new Timer(DELAY, this);
        timer.start();

	}

	@Override
	public void paintComponent(Graphics g) {
		super.paintComponent(g);
		doDrawing(g);
	}

	private void doDrawing(Graphics g) {

		for (int z = 0; z < dogs1.size(); z++) {

			g.drawImage(dogs1.get(z).icon.getImage(), x[z], y[z], this);        
			
			
		}
		for (int z = 0; z < dogshit.size(); z++) {

			g.drawImage(dogshit.get(z).icon.getImage(), x[z], y[z], this);        
			 
			
		}
		for (int z = 0; z < food.size(); z++) {

			g.drawImage(food.get(z).icon.getImage(), x[z], y[z], this);
		}
		Toolkit.getDefaultToolkit().sync();
	}
	

//	private void gameOver(Graphics g) {
//
//		String msg = "Game Over";
//		Font small = new Font("Helvetica", Font.ITALIC, 130);
//		FontMetrics metr = getFontMetrics(small);
//
//		g.setColor(Color.white);
//		g.setFont(small);
//		g.drawString(msg, (B_WIDTH - metr.stringWidth(msg)) / 5, B_HEIGHT / 2);
//
//	}

	
	private void move() {

        for (int z = Dogs; z > 0; z--) {
            x[z] = x[(z - 1)];
            y[z] = y[(z - 1)];
        }

        if (leftDirection) {
            x[0] -= DOG_SIZE;
        }

        if (rightDirection) {
            x[0] += DOG_SIZE;
        }

        if (upDirection) {
            y[0] -= DOG_SIZE;
        }

        if (downDirection) {
            y[0] += DOG_SIZE;
        }
        
        count++;
        Random rd = new Random();
        Random rand = new Random();

      

        int randomNum = rand.nextInt((20 - 1) + 1) + 1;
        int randomNum1 = rand.nextInt((50 - 1) + 1) + 1;
       
        if(count % randomNum == 0) {
        	upDirection = rd.nextBoolean();
	        rightDirection = rd.nextBoolean();
	        leftDirection = rd.nextBoolean();
	        downDirection = rd.nextBoolean();
        }
        
        //if(count % randomNum1 == 0) {
        //	randomShit(dogs1.get(0), getGraphics());
      //  }
        
        if(upDirection == false && downDirection == false && leftDirection == false && rightDirection == false) {
        	rightDirection = false;
        }
        if(upDirection == true && downDirection == true && leftDirection == true && rightDirection == true) {
        	rightDirection = true;
        	upDirection = false;
        	downDirection = false;
        	leftDirection = false;
        }
        
       
 	   	
    }
	
	private void checkFood() {

		if ((x[0] == food_x) && (y[0] == food_y)) {

			inGame = false;
			food.add(new Dog().new Food());
			shitScore ++;
			locateFood();

		}

	}
	private void checkFood() {
		   
		   for(Food t : food) {
	    		
	    		if ((x[0] == t.food_x) && (y[0] == t.food_y) || (x1[0] == t.food_x) && (y1[0] == t.food_y)) {
	            	
	    			randomShit(dogs1.get(0), getGraphics());
	    			
	            	
	            }
	    	}
	        
	   }
	
//	private void shitScoreBoard() {
//
//		
//		if (shitScore == 3) {
//			
//			dogshit.add(new Shit());
//
//			locateShit();
//		}
//
//	}
	
	
	private void checkShit() {

		if ((x[0] == shit_x) && (y[0] == shit_y)) {

			//inGame = false;
			

		}

	}
	
//	private void locateFood() {
//
//		int r = (int) (Math.random() * RAND_POS);
//		food_x = ((r * DOG_SIZE));
//
//		r = (int) (Math.random() * RAND_POS);
//		food_y = ((r * DOG_SIZE));
//		
//		
//		
//	}
	
	private void locateFood() {
	   	Random rd = new Random();
//    	isBomb = false;
    	int b = (int) (Math.random() * 50);
        int food_x = ((b * DOG_SIZE));

        b = (int) (Math.random() * 50);
        int food_y = ((b * DOG_SIZE));
        
        food.add(new Dog().new Food(new Point(food_x,food_y)));
        
    }
	
//	public void randomShit(Dog d, Graphics g) {
//
//		  
//		   Dog.Food f = new Dog().new Food(new Point());
//		   Dog.Shit s = d.eat(f);
//		   s.setLocation(new Point(x[0],y[0]));
//		   dogshit.add(s);
//		   
//	   }
	
	private void locateShit() {

		int a = (int) (Math.random() * RAND_POS);
		shit_x = ((a * DOG_SIZE));

		a = (int) (Math.random() * RAND_POS);
		shit_y = ((a * DOG_SIZE));
		
		food.add(new (food_x,food_y));
		
	}
	
	
	private void checkCollision() {

    	for (int z = Dogs; z > 0; z--) {

    	    if ((z > 4) && (x[0] == x[z]) && (y[0] == y[z])) {
    	        isRunning = false;
    	    }
    	}
    	Random rd = new Random();

        if (y[0] >= B_HEIGHT) {
//            isRunning = false;
        	upDirection = rd.nextBoolean();
            rightDirection = rd.nextBoolean();
            leftDirection = rd.nextBoolean();
            downDirection = false;
        }

        if (y[0] < 0) {
//            isRunning = false;
        	leftDirection = rd.nextBoolean();
            upDirection = false;
            downDirection = rd.nextBoolean();
            rightDirection = rd.nextBoolean();
        }

        if (x[0] >= B_WIDTH) {
//        	isRunning = false;
        	upDirection = rd.nextBoolean();
            rightDirection = false;
            leftDirection = rd.nextBoolean();
            downDirection = rd.nextBoolean();
        }

        if (x[0] < 0) {
//            isRunning = false;
        	leftDirection = false;
            upDirection = rd.nextBoolean();
            downDirection = rd.nextBoolean();
            rightDirection = rd.nextBoolean();
        }
        
        if (!isRunning) {
            timer.stop();
        }
    }
	  @Override
	   public void actionPerformed(ActionEvent e) {

	        if (isRunning) {
	        	//checkFood();
	        	checkShit();
	            checkCollision();
	            move();
	        }
	        repaint();
	    }
	  
	  private class TAdapter extends KeyAdapter {

	        @Override
	        public void keyPressed(KeyEvent e) {

	            int key = e.getKeyCode();
	            
	            if ((key == KeyEvent.VK_S) && (!upDirection)) {
	                downDirection = true;
	                rightDirection = false;
	                leftDirection = false;
	            }
	            
	            if ((key == KeyEvent.VK_A) && (!rightDirection)) {
	                leftDirection = true;
	                upDirection = false;
	                downDirection = false;
	            }

	            if ((key == KeyEvent.VK_D) && (!leftDirection)) {
	                rightDirection = true;
	                upDirection = false;
	                downDirection = false;
	            }

	            if ((key == KeyEvent.VK_W) && (!downDirection)) {
	                upDirection = true;
	                rightDirection = false;
	                leftDirection = false;
	            } 
	            if ((key == KeyEvent.VK_ENTER && (!isRunning))) {
	            	
	            	
	            }
	        }
	    }

}
