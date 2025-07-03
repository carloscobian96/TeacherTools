package csi.irene.snake;

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
import javax.swing.ImageIcon;
import javax.swing.JPanel;
import javax.swing.Timer;

public class Board extends JPanel implements ActionListener {

	private int Score = 0;
	private final int B_WIDTH = 900;
	private final int B_HEIGHT = 900;
	private final int DOT_SIZE = 50;
	private final int ALL_DOTS = 50;
	private final int RAND_POS = 10;
	private final int DELAY = 140;

	private final int x[] = new int[ALL_DOTS];
	private final int y[] = new int[ALL_DOTS];

	private int dots;
	private int apple_x;
	private int apple_y;
	private int Mine_x;
	private int Mine_y;
	private int Mine2_x;
	private int Mine2_y;
	private boolean startOver;
	private boolean leftDirection = false;
	private boolean rightDirection = true;
	private boolean upDirection = false;
	private boolean downDirection = false;
	private boolean inGame = true;
	private Timer timer;
	private Image ball;
	private Image apple;
	private Image head;
	private Image background;
	private Image background2;
	private Image Mine;
	private Image Mine2;

	public Board() {

		initBoard();
	}

	private void initBoard() {

		addKeyListener(new TAdapter());
		setBackground(new Color(0, 150, 150));
		setFocusable(true);

		setPreferredSize(new Dimension(B_WIDTH, B_HEIGHT));
		loadImages();
		initGame();
	}

	private void loadImages() {

		ImageIcon iid = new ImageIcon(getClass().getResource("Level.png"));
		ball = iid.getImage();

		ImageIcon iia = new ImageIcon(getClass().getResource("Chest.png"));
		apple = iia.getImage();

		ImageIcon iih = new ImageIcon(getClass().getResource("DarkSouls.png"));
		head = iih.getImage();

		ImageIcon iib = new ImageIcon(getClass().getResource("Do.png"));
		background = iib.getImage();
		ImageIcon iic = new ImageIcon(getClass().getResource("Dungeon.png"));
		background2 = iic.getImage();

		ImageIcon iie = new ImageIcon(getClass().getResource("Enemy.png"));
		Mine = iie.getImage();
		
		ImageIcon iif = new ImageIcon(getClass().getResource("Enemy.png"));
		Mine = iif.getImage();
		
		
		
		
	}

	private void initGame() {

		dots = 3;

		for (int z = 0; z < dots; z++) {
			x[z] = 50 - z * 10;
			y[z] = 50;

		}

		locateApple();
		locateMine();
		
		timer = new Timer(DELAY, this);
		timer.start();

	}

	@Override
	public void paintComponent(Graphics g) {
		super.paintComponent(g);

		g.drawImage(background2, 0, 0, null);
		doDrawing(g);

		if (!inGame) {
			timer.stop();
			g.drawImage(background, 0, 0, null);
			doDrawing(g);

		}
	}

	private void doDrawing(Graphics g) {

		if (inGame) {

			g.drawImage(apple, apple_x, apple_y, this);

			for (int z = 0; z < dots; z++) {
				if (z == 0) {
					g.drawImage(head, x[z], y[z], this);
				} else {
					g.drawImage(ball, x[z], y[z], this);
				}
				 g.drawImage(Mine, Mine_x, Mine_y, this);
				
			}
			Score(g);
			Toolkit.getDefaultToolkit().sync();
			g.drawImage(Mine2, Mine2_x, Mine2_y, this);
		}
		
		else {

			gameOver(g);
			startOver(g);

		}
	}

	private void gameOver(Graphics g) {

		String msg = "Game Over";
		Font small = new Font("Roman Baselina", Font.ROMAN_BASELINE, 60);
		FontMetrics metr = getFontMetrics(small);

		g.setColor(Color.RED);
		g.setFont(small);
		g.drawString(msg, (B_WIDTH - metr.stringWidth(msg)) / 2, B_HEIGHT / 2);

	}

	private void startOver(Graphics g) {

		String msg = "Start Over";
		Font small = new Font("ITALIC", Font.ITALIC, 60);
		FontMetrics metr = getFontMetrics(small);

		g.setColor(Color.BLUE);
		g.setFont(small);
		g.drawString(msg, (B_WIDTH - metr.stringWidth(msg)) / 2, B_HEIGHT / 4);

	}

	private void Score(Graphics g) {

		String msg = "Dungeon " + Score;
		Font small = new Font("Roman", Font.ROMAN_BASELINE, 40);
		FontMetrics metr = getFontMetrics(small);

		g.setColor(Color.WHITE);
		g.setFont(small);
		g.drawString(msg, (B_WIDTH - metr.stringWidth(msg)) / 2, B_HEIGHT / 13);

	}

	private void checkApple() {

		if ((x[0] == apple_x) && (y[0] == apple_y)) {

			dots++;
			Score++;
			locateApple();
		}
	}

	private void checkMine() {

		if ((x[0] == Mine_x) && (y[0] == Mine_y)) {
			inGame = false;
			locateMine();
			timer.stop();

		}
	}
	
		
		
	

	private void move() {

		for (int z = dots; z > 0; z--) {
			x[z] = x[(z - 1)];
			y[z] = y[(z - 1)];
		}

		if (leftDirection) {
			x[0] -= DOT_SIZE;
		}

		if (rightDirection) {
			x[0] += DOT_SIZE;
		}

		if (upDirection) {
			y[0] -= DOT_SIZE;
		}

		if (downDirection) {
			y[0] += DOT_SIZE;
		}
		
//		random
//		ld
//		rd
//		ud
//		dd
	}

	private void checkCollision() {

		for (int z = dots; z > 0; z--) {

			if ((z > 4) && (x[0] == x[z]) && (y[0] == y[z])) {
				inGame = false;
			}
		}

		if (y[0] >= B_HEIGHT) {
			inGame = false;
		}

		if (y[0] < 0) {
			inGame = false;
		}

		if (x[0] >= B_WIDTH) {
			inGame = false;
		}

		if (x[0] < 0) {
			inGame = false;
		}

		if (!inGame) {
			timer.stop();
		}
	}

	private void locateApple() {

		int r = (int) (Math.random() * RAND_POS);
		apple_x = ((r * DOT_SIZE));

		r = (int) (Math.random() * RAND_POS);
		apple_y = ((r * DOT_SIZE));
	}

	private void locateMine() {

		int e = (int) (Math.random() * RAND_POS);
		Mine_x = ((e * DOT_SIZE));

		e = (int) (Math.random() * RAND_POS);
		Mine_y = ((e * DOT_SIZE));
	}

	@Override
	public void actionPerformed(ActionEvent e) {

		if (inGame) {

			checkApple();
			checkCollision();
			move();

			checkMine();
            
		}

		repaint();
	}

	private class TAdapter extends KeyAdapter {

		@Override
		public void keyPressed(KeyEvent e) {

			int key = e.getKeyCode();

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

			if ((key == KeyEvent.VK_S) && (!upDirection)) {
				downDirection = true;
				rightDirection = false;
				leftDirection = false;
			}

			if ((key == KeyEvent.VK_ENTER)) {
				inGame = true;
				timer.stop();
				initGame();
				Score = 0;
				downDirection = false;
				rightDirection = true;
				leftDirection = false;
				upDirection = false;
			}
				
				
				
			}
		}
	}


