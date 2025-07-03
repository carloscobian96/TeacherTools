
package csi.negron.snake;

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
import java.util.Random;

import javax.swing.ImageIcon;
import javax.swing.JPanel;
import javax.swing.Timer;

public class Board extends JPanel implements ActionListener {

	private final int B_WIDTH = 1000;
	private final int B_HEIGHT = 600;
	private final int DOT_SIZE = 50;
	private final int ALL_DOTS = 900;
	private final int RAND_POS = 10;
	private final int DELAY = 140;

	private final int x[] = new int[ALL_DOTS];
	private final int y[] = new int[ALL_DOTS];

	private int dots;
	private int apple_x;
	private int apple_y;
	private int mine_x;
	private int mine_y;

	private boolean leftDirection = false;
	private boolean rightDirection = true;
	private boolean upDirection = false;
	private boolean downDirection = false;
	private boolean inGame = true;

	private int score = 0;

	private Timer timer;
	private Image ball;
	private Image apple;
	private Image head;
	private Image background;
	private Image mine;

	Color[] arr = { Color.RED, Color.YELLOW, Color.CYAN, new Color(164, 27, 255) };

	public Board() {

		initBoard();
	}

	private void initBoard() {

		addKeyListener(new TAdapter());
		setBackground(new Color(27, 225, 255));
		setFocusable(true);

		setPreferredSize(new Dimension(B_WIDTH, B_HEIGHT));
		loadImages();
		initGame();
	}

	private void loadImages() {

		ImageIcon iid = new ImageIcon(getClass().getResource("body.png"));
		ball = iid.getImage();

		ImageIcon iia = new ImageIcon(getClass ().getResource("apple.png"));
		apple = iia.getImage();

		ImageIcon iih = new ImageIcon(getClass ().getResource("head.gif"));
		head = iih.getImage();

		ImageIcon iib = new ImageIcon(getClass().getResource("mine.png"));
		mine = iib.getImage();

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

	private void scoreBoard(Graphics g) {

		String scoreboard = "Current Score: " + score + "     ";
		Font smallA = new Font("Helvetica", Font.ITALIC, 20);
		FontMetrics metrA = getFontMetrics(smallA);

		if (score == 5) {

		}

		g.setColor(Color.black);
		g.setFont(smallA);
		g.drawString(scoreboard, (B_WIDTH - metrA.stringWidth(scoreboard)) / 1, B_HEIGHT / 10);

	}

	public void restart() {

		inGame = true;
		initGame();
		score = 0;

		rightDirection = true;
		upDirection = false;
		downDirection = false;
		leftDirection = false;

	}

	@Override
	public void paintComponent(Graphics g) {
		super.paintComponent(g);
		g.drawImage(background, 0, 0, null);
		doDrawing(g);
	}

	private void doDrawing(Graphics g) {

		if (inGame) {

			g.drawImage(apple, apple_x, apple_y, this);
			g.drawImage(mine, mine_x, mine_y, this);

			for (int z = 0; z < dots; z++) {
				if (z == 0) {
					g.drawImage(head, x[z], y[z], this);
				} else {
					g.drawImage(ball, x[z], y[z], this);
				}

			}
			scoreBoard(g);

			Toolkit.getDefaultToolkit().sync();

		} else {

			gameOver(g);
		}
	}

	private void gameOver(Graphics g) {

		String msg = "You Died";
		String mma = "Try Again";
		Font small = new Font("Helvetica", Font.BOLD, 36);
		FontMetrics metr = getFontMetrics(small);

		g.setColor(Color.black);
		g.setFont(small);
		g.drawString(msg, (B_WIDTH - metr.stringWidth(msg)) / 2, B_HEIGHT / 3);
		g.drawString(mma, (B_WIDTH - metr.stringWidth(mma)) / 2, B_HEIGHT / 2);
	}

	private void checkApple() {

		if ((x[0] == apple_x) && (y[0] == apple_y)) {

			int index = new Random().nextInt(arr.length);
			setBackground(arr[index]);
			dots++;
			score++;
			locateApple();
			locateMine();
		}

	}

	private void checkMine() {

		if ((x[0] == mine_x) && (y[0] == mine_y)) {

			inGame = false;
			locateMine();

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

		int a = (int) (Math.random() * RAND_POS);
		mine_x = ((a * DOT_SIZE));

		a = (int) (Math.random() * RAND_POS);
		mine_y = ((a * DOT_SIZE));
	}

	@Override
	public void actionPerformed(ActionEvent e) {

		if (inGame) {

			checkApple();
			checkMine();
			checkCollision();
			move();
		}

		repaint();
	}

	private class TAdapter extends KeyAdapter {

		@Override
		public void keyPressed(KeyEvent e) {

			int key = e.getKeyCode();

			if ((key == KeyEvent.VK_LEFT) && (!rightDirection)) {
				leftDirection = true;
				upDirection = false;
				downDirection = false;
			}

			if ((key == KeyEvent.VK_RIGHT) && (!leftDirection)) {
				rightDirection = true;
				upDirection = false;
				downDirection = false;
			}

			if ((key == KeyEvent.VK_UP) && (!downDirection)) {
				upDirection = true;
				rightDirection = false;
				leftDirection = false;
			}

			if ((key == KeyEvent.VK_DOWN) && (!upDirection)) {
				downDirection = true;
				rightDirection = false;
				leftDirection = false;
			}
			if ((key == KeyEvent.VK_ENTER && (!inGame))) {
				restart();
			}
		}
	}
}
