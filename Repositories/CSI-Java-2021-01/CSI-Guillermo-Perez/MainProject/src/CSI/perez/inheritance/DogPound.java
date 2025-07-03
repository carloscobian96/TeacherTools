package csi.perez.inheritance;

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

import csi.perez.inheritance.Dog.Food;

public class DogPound extends JPanel implements ActionListener {

	private static final double RAND_POS = 0;
	List<Dog> dogs1 = new ArrayList<Dog>();
	List<Dog.Shit> shit1 = new ArrayList<Dog.Shit>();
	List<Food> food1 = new ArrayList<Food>();

	private int B_WIDTH = 1000;
	private int B_HEIGHT = 700;
	private int DOG_SIZE = 50;
	private int ALL_DOGS = 120;

	private final int x[] = new int[ALL_DOGS];
	private final int y[] = new int[ALL_DOGS];

//	private final int x1[] = new int[ALL_SHITS];
//	private final int y1[] = new int[ALL_SHITS];

	private int dogs;
//	

	private boolean leftDirection = false;
	private boolean rightDirection = true;
	private boolean upDirection = false;
	private boolean downDirection = false;
	private boolean isRunning = true;

	private Timer timer;
	private final int DELAY = 140;

	private int count;

	public DogPound() {
		dogs1.add(new GoldenDoodle());

		initBoard();
	}

	private void initBoard() {

		addKeyListener(new TAdapter());
		setBackground(new Color(255, 255, 255));
		setFocusable(true);

		setPreferredSize(new Dimension(B_WIDTH, B_HEIGHT));
		initSimulation();
	}

	private void initSimulation() {

		dogs = 1;

		for (int z = 0; z < dogs; z++) {
			x[z] = 50 - z * 10;
			y[z] = 50;
		}

		timer = new Timer(DELAY, this);
		timer.start();

	}

	@Override
	public void paintComponent(Graphics g) {
		super.paintComponent(g);

		doDrawing(g);
	}

	private void doDrawing(Graphics g) {

//		Coge la imagen de dog y la implementa en el window del juego	
		for (int z = 0; z < dogs; z++) {

			g.drawImage(dogs1.get(z).icon.getImage(), x[z], y[z], this);

		}

		for (int z = 0; z < food1.size(); z++) {

			g.drawImage(food1.get(z).icon.getImage(), food1.get(z).point.x, food1.get(z).point.y, this);

		}

		Toolkit.getDefaultToolkit().sync();
	}

	private void checkFood() {

		for (int z = 0; z < food1.size(); z++) {

			if (food1.get(z).point.x == x[0]  &&  food1.get(z).point.y == y[0]   ) {
				System.out.println("nom");
				
			}

		}
	}
//	 public Rectangle getBounds() {
//	        return new Rectangle(x, y, width, height);
//	    }
	private void move() {

		for (int z = dogs; z > 0; z--) {
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

		Random rand = new Random();
		int m = rand.nextInt(6);

		if (m == 1) {
			upDirection = true;
			rightDirection = false;
			leftDirection = false;
			downDirection = false;
		}
		if (m == 2) {
			upDirection = false;
			rightDirection = true;
			leftDirection = false;
			downDirection = false;
		}
		if (m == 3) {
			upDirection = false;
			rightDirection = false;
			leftDirection = true;
			downDirection = false;
		}
		if (m == 4) {
			upDirection = false;
			rightDirection = false;
			leftDirection = false;
			downDirection = true;
		}
		if (m == 5) {
			upDirection = false;
			rightDirection = false;
			leftDirection = false;
			downDirection = false;
		}
		if (m == 6) {
			upDirection = false;
			rightDirection = false;
			leftDirection = false;
			downDirection = false;
		}

	}

	private void checkCollision() {

		for (int z = dogs; z > 0; z--) {

			if ((z >= 2) && (x[0] == x[z]) && (y[0] == y[z])) {

			}
		}

		if (y[0] >= B_HEIGHT) {
			y[0] -= DOG_SIZE;
		}

		if (y[0] < 0) {
			y[0] += DOG_SIZE;
		}

		if (x[0] >= B_WIDTH) {
			x[0] -= DOG_SIZE;
		}

		if (x[0] < 0) {
			x[0] += DOG_SIZE;
		}

	}

	private void locateFood() {

		Random rand = new Random();
		int x = rand.nextInt(B_WIDTH);
		int y = rand.nextInt(B_HEIGHT);

		food1.add(new Dog().new Food(new Point(x, y)));

//     
	}

	@Override
	public void actionPerformed(ActionEvent e) {

		if (isRunning) {
			checkCollision();
			move();
		}

		if (food1.size() < 5) {
			
			locateFood();
			
		}
		repaint();
	}

	private void CheckFood() {

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
