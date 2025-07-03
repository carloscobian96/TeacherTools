package csi.lopez.sim;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.EventQueue;
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
import java.util.*;

import javax.swing.ImageIcon;
import javax.swing.JPanel;
import javax.swing.Timer;

import csi.lopez.sim.Dog.Food;
import csi.lopez.snake.Bomb;

public class DogPound extends JPanel implements ActionListener{
	
	List<Dog> dogs1 = new ArrayList<Dog>();
	List<Dog.Shit> dogshits = new ArrayList<Dog.Shit>();
	List<Treat> treats = new ArrayList<Treat>();
	List<Dog.Piss> pisses = new ArrayList<Dog.Piss>();
	
	private int B_WIDTH = 800;
	private int B_HEIGHT = 800; 
	private int DOG_SIZE = 10;
	private int ALL_DOGS = 120;
	
	private final int x[] = new int[ALL_DOGS];
    private final int y[] = new int[ALL_DOGS];
    
	private final int x1[] = new int[ALL_DOGS];
    private final int y1[] = new int[ALL_DOGS];
	
    private int dogs;
    
    private boolean leftDirection = false;
    private boolean rightDirection = true;
    private boolean upDirection = false;
    private boolean downDirection = false;
    
    private boolean leftDirection1 = false;
    private boolean rightDirection1 = true;
    private boolean upDirection1 = false;
    private boolean downDirection1 = false;
    
    private boolean isRunning = true;
    
    
    private boolean isShit = true;
    private boolean angered = false;
    private  boolean isPreg = false;
    private boolean needsToPiss = false;
    
    private Timer timer;
    private final int DELAY = 140;
    
    private int count; 
    
    private Point startP = setStartP(new Point(100, 100));
    

	
	public Point getStartP() {
		return startP;
	}

	public Point setStartP(Point startP) {
		return this.startP = startP;
	}

	private Image shepherd; 
	private Image icon;
	public ImageIcon treat = new ImageIcon(new ImageIcon(getClass().getResource("treat.png")).getImage().getScaledInstance(50, 50,  java.awt.Image.SCALE_SMOOTH));
	public ImageIcon piss = new ImageIcon(new ImageIcon(getClass().getResource("piss.png")).getImage().getScaledInstance(50, 50,  java.awt.Image.SCALE_SMOOTH));

	
	  public DogPound() {
	        dogs1.add(new GermanShepherd(startP));
	        
	        
	        initBoard();
	    }
	    
	   private void initBoard() {
		   
//	        addKeyListener(new TAdapter());
	        setBackground(new Color(50, 150, 150));
	        setFocusable(true);

	        setPreferredSize(new Dimension(B_WIDTH, B_HEIGHT));
	        initSimulation();
	        
//	        loadImages();
	        
	    }
	   
	   private void initSimulation() {

	        dogs = 1;

	        for (int z = 0; z < dogs; z++) {
	            x[z] = 150 - z * 10;
	            y[z] = 150;
	            
	            x1[z] = 150 - z * 10;
	            y1[z] = 150;
	            
	            
	        }
	        
	  
	        
	        locateTreat();
//	        checkFood();
	        
	        timer = new Timer(DELAY, this);
	        timer.start();
	   }
	   
//	   
//	   public void loadImages() {
//
//	        ImageIcon iid = new ImageIcon(getClass().getResource("GermanShepherd.png"));
//	        shepherd = iid.getImage().getScaledInstance(120, 120,  java.awt.Image.SCALE_SMOOTH);
//	        iid = new ImageIcon(shepherd);
//	        
//	   }
//	  
	   
	   
	   @Override
	   public void paintComponent(Graphics g) {
		   super.paintComponent(g);
		   
//		   g.drawImage(shepherd, 0, 0, null);
		   doDrawing(g);
	   }
	   
	   private void doDrawing(Graphics g) {
		   
		   
		   
		   if (isRunning) {
			   
			   for(Treat t : treats) {
	            	g.drawImage(treat.getImage(), t.food_x, t.food_y, this);

	            }
			  
	            
			   
	            for (int z = 0; z < dogs1.size(); z++) {
	            	int b = Math.round(dogs1.get(z).getAlignmentX());
	            	int a = Math.round(dogs1.get(z).getAlignmentY());
//	            	System.out.println(b);

//                    g.drawImage(dogs1.get(z).icon.getImage(), b, a, this);
                    g.drawImage(dogs1.get(z).icon.getImage(), x[z], y[z], this);
                    g.drawImage(dogs1.get(z).icon.getImage(), x1[z], y1[z], this);

                    
                    

	               
	            }
	            

	            
	            //Dog shit	
	            for (int z = 0; z < dogshits.size(); z++) {
	    	            
		            g.drawImage(dogshits.get(z).icon.getImage(), dogshits.get(z).getLocation().x,  dogshits.get(z).getLocation().y, null);
		                    
		           }
	            
	            //Bark
	            if(angered == true) {
	            	bark(g);
	            }
	            //Piss
//	            if(needsToPiss == true) {
//	            	randomPiss(g);
//	            }
	            //Piss again 
	            for(int z = 0; z < pisses.size(); z++) {
	            	g.drawImage(piss.getImage(), pisses.get(z).getLocation().x, pisses.get(z).getLocation().y, this);
	            }
	            //mate test
	            if(isPreg == true) {
	            	preg(g);
	            }
	            
	            Toolkit.getDefaultToolkit().sync();
		   } else {
			   
		   }
		   

	   }
	   
	   private void checkFood() {
		   
		   for(Treat t : treats) {
	    		
	    		if ((x[0] == t.food_x) && (y[0] == t.food_y) || (x1[0] == t.food_x) && (y1[0] == t.food_y)) {
	            	
	    			randomShit(dogs1.get(0), getGraphics());
	    			
	            	
	            }
	    	}
	        
	   }
	   
	   
//	   private void gameOver(Graphics g) {
//	    	
//	        String msg = "Game Over";
//	        Font small = new Font("Helvetica", Font.ITALIC, 130);
//        FontMetrics metr = getFontMetrics(small);
//	
//	        g.setColor(Color.white);
//	        g.setFont(small);
//	        g.drawString(msg, (B_WIDTH - metr.stringWidth(msg)) / 5, B_HEIGHT / 2);
//	        
//	    
//	    }
	   
	    
	   public void randomShit(Dog d, Graphics g) {
//		   int z = dogs;
		  
		   Dog.Food f = (new Dog()).new Food();
		   Dog.Shit s = d.eat(f);
		   s.setLocation(new Point(x[0],y[0]));
		   dogshits.add(s);
		   
	   }
	   
	   public void randomPiss(Graphics g, Dog d) {
//		   int piss_x = x[0];
//		   int piss_y = y[0];
//		  g.drawImage(piss.getImage(), piss_x, piss_y, this);
		   Dog.Piss f = (new Dog()).new Piss();
		   f.setLocation(new Point(x[0], y[0]));
		   pisses.add(f);
		   
	   }
	   
	   private void locateTreat() {
		   	Random rd = new Random();
//	    	isBomb = false;
	    	int b = (int) (Math.random() * 50);
	        int food_x = ((b * DOG_SIZE));

	        b = (int) (Math.random() * 50);
	        int food_y = ((b * DOG_SIZE));
	        
	        treats.add(new Treat(food_x,food_y));
	        
	    }
	   
	   private void move() {

	        for (int z = dogs; z > 0; z--) {
	            x[z] = x[(z - 1)];
	            y[z] = y[(z - 1)]; 
	            
	            x1[z] = x1[(z - 1)];
	            y1[z] = y1[(z - 1)]; 
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
	        // second doggo
	        if (leftDirection1) {
	            
	            x1[0] += DOG_SIZE;
	        }

	        if (rightDirection1) {
	            
	            x1[0] -= DOG_SIZE;
	        }

	        if (upDirection1) {
	           
	            y1[0] += DOG_SIZE;
	        }

	        if (downDirection1) {
	           
	            y1[0] -= DOG_SIZE;
	        }
	
	        count++;
	        Random rd = new Random();
	        Random rand = new Random();
	        
	        //random for dog 1
	        int randomNum = rand.nextInt((30 - 1) + 1) + 1;
	        //random for food
	        int randomNum1 = rand.nextInt((5000 - 1) + 1) + 1;
	        //random for dog 2
	        int randomNum2 = rand.nextInt((100 - 1) + 1) + 1;
	        //random for piss
	        int needPiss = rand.nextInt((500 - 1) + 1) + 1;
	       
	        if(count % randomNum == 0) {
	        	upDirection = rd.nextBoolean();
		        rightDirection = rd.nextBoolean();
		        leftDirection = rd.nextBoolean();
		        downDirection = rd.nextBoolean();
		        
	        }
	        
	        if(count % randomNum2 == 0) {
	        	upDirection1 = rd.nextBoolean();
		        rightDirection1 = rd.nextBoolean();
		        leftDirection1 = rd.nextBoolean();
		        downDirection1 = rd.nextBoolean();
	        }
	        if(count % randomNum1 == 1) {
	        	locateTreat();
	        }
	        
	        if(count % randomNum == 2) {
	        	angered = true;
	        }
	        
	        if(count % needPiss == 0) {
	        	needsToPiss = true; 
	        }
	        
	      	   	
	    }
	   public void mate(){
		   if ((x[0] == x1[0]) && (y[0] == y1[0])){
			   isPreg = true;
		   }
		   
	   }
	   
	   private void preg(Graphics g) {
		   
		   String msgP = "is preg";
		   Font smallP = new Font("Helvetica", Font.ITALIC, 20);
		   
		   g.setFont(smallP);
		   g.drawString(msgP, x1[0], y1[0]);
	   }
	   private void bark(Graphics g) {
		   

	    	 String msgA = "Grrrrruuuaaaa!!!";
	    	 Font smallA = new Font("Helvetica", Font.ITALIC, 20);
	    	 
	    	
	    	 String msgB = "Grrrrrr!!!";
	    	 Font smallB = new Font("Helvetica", Font.ITALIC, 25);

	         g.setColor(Color.black);
	         g.setFont(smallA);
	         g.drawString(msgA, x[0], y[0]);
	         dogs1.get(0).bark();
	         
	         if(count % 2 == 0 && isPreg == false) {
	        	 g.setFont(smallB);
		         g.drawString(msgB, x1[0], y1[0]);
		         dogs1.get(0).bark();
	    	 }
	         
	         
	         if(count % 15 == 0) {
	        	  angered = false;
	         }
	       
		   
	   }
	   
	   
	   
	   
	   private void checkCollision() {

	    	for (int z = dogs; z > 0; z--) {

	    	    if ((z > 4) && (x[0] == x[z]) && (y[0] == y[z])) {
	    	        isRunning = false;
	    	    }
	    	}
	    	Random rd = new Random();

	        if (y[0] >= B_HEIGHT) {
//	            isRunning = false;
	        	upDirection = rd.nextBoolean();
                rightDirection = rd.nextBoolean();
                leftDirection = rd.nextBoolean();
                downDirection = false;
	        }

	        if (y[0] < 0) {
//	            isRunning = false;
	        	leftDirection = rd.nextBoolean();
                upDirection = false;
                downDirection = rd.nextBoolean();
                rightDirection = rd.nextBoolean();
	        }

	        if (x[0] >= B_WIDTH) {
//	        	isRunning = false;
	        	upDirection = rd.nextBoolean();
                rightDirection = false;
                leftDirection = rd.nextBoolean();
                downDirection = rd.nextBoolean();
	        }

	        if (x[0] < 0) {
//	            isRunning = false;
	        	leftDirection = false;
                upDirection = rd.nextBoolean();
                downDirection = rd.nextBoolean();
                rightDirection = rd.nextBoolean();
	        }
	        // Second Dog 
	        
	        if(x1[0] < 0) {
	        	leftDirection1 = rd.nextBoolean();
                upDirection1 = rd.nextBoolean();
                downDirection1 = rd.nextBoolean();
                rightDirection1 = false;
	        }
	        
	        if( x1[0] >= B_WIDTH) {
	        	upDirection1 = rd.nextBoolean();
                rightDirection1 = rd.nextBoolean();
                leftDirection1 = false;
                downDirection1 = rd.nextBoolean();
	        }
	        
	        if( y1[0] < 0) {
	        	leftDirection1 = rd.nextBoolean();
                upDirection1 = rd.nextBoolean();;
                downDirection1 = false;
                rightDirection1 = rd.nextBoolean();
	        }
	        
	        if( y1[0] >= B_HEIGHT) {
	        	upDirection1 = false;
                rightDirection1 = rd.nextBoolean();
                leftDirection1 = rd.nextBoolean();
                downDirection1 = rd.nextBoolean();
	        }
	        
	        if (!isRunning) {
	            timer.stop();
	        }
	    }
	   
	   
	   @Override
	   public void actionPerformed(ActionEvent e) {

	        if (isRunning) {
	            checkCollision();
	            move();
	            checkFood();
	            mate();
	        }
	        repaint();
	    }
	   
//	   private class TAdapter extends KeyAdapter {
//
//	        @Override
//	        public void keyPressed(KeyEvent e) {
//
//	            int key = e.getKeyCode();
//	            
//	            if ((key == KeyEvent.VK_S) && (!upDirection)) {
//	                downDirection = true;
//	                rightDirection = false;
//	                leftDirection = false;
//	            }
//	            
//	            if ((key == KeyEvent.VK_A) && (!rightDirection)) {
//	                leftDirection = true;
//	                upDirection = false;
//	                downDirection = false;
//	            }
//
//	            if ((key == KeyEvent.VK_D) && (!leftDirection)) {
//	                rightDirection = true;
//	                upDirection = false;
//	                downDirection = false;
//	            }
//
//	            if ((key == KeyEvent.VK_W) && (!downDirection)) {
//	                upDirection = true;
//	                rightDirection = false;
//	                leftDirection = false;
//	            } 
//	            if ((key == KeyEvent.VK_ENTER && (!isRunning))) {
//	            	
//	            	
//	            }
//	        }
//	    }
	   
	   
	   public class Treat {

		    public int food_x;
		    public int food_y;
		   
		    
			public Treat(int food_x, int food_y) {
				super();
				this.food_x = food_x;
				this.food_y = food_y;
//				this.treat = new ImageIcon(new ImageIcon(getClass().getResource("treat.png")).getImage().getScaledInstance(50, 50,  java.awt.Image.SCALE_SMOOTH));
			}
			
	   }
	   
	   public class Piss {
		   public int piss_x;
		   public int piss_y;
		   
		   
		   public Piss(int piss_x, int piss_y) {
			   super();
			   this.piss_x = piss_x;
			   this.piss_y = piss_y;
		   }
	   }
	
}
