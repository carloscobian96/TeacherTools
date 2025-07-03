package csi.lopez.snake;

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

import javax.swing.ImageIcon;
import javax.swing.JPanel;
import javax.swing.Timer;

import csi.lopez.life1.Loan;

import javax.swing.JButton;

public class Board extends JPanel implements ActionListener {

    private final int B_WIDTH = 800;
    private final int B_HEIGHT = 800;
    private final int DOT_SIZE = 50;
    private final int ALL_DOTS = 50;
    private final int RAND_POS = 12;
    private final int DELAY = 140;

    private final int x[] = new int[ALL_DOTS];
    private final int y[] = new int[ALL_DOTS];

    private int dots;
    private int apple_x;
    private int apple_y;
    
    List<Bomb> bombs = new ArrayList<Bomb>();
    
    
    private int score = 0;
    
    private boolean leftDirection = false;
    private boolean rightDirection = true;
    private boolean upDirection = false;
    private boolean downDirection = false;
    private boolean inGame = true;
    
    private boolean isBomb = false;
    private int numberOfBombs = bombs.size();

    private Timer timer;
    private Image ball;
    private Image apple;
    private Image head;
    private Image background;
    private Image meme;
    private Image bomb;
   

    public Board() {
        
        initBoard();
    }
    
    private void initBoard() {

        addKeyListener(new TAdapter());
        setBackground(new Color(50, 150, 150));
        setFocusable(true);

        setPreferredSize(new Dimension(B_WIDTH, B_HEIGHT));
        loadImages();
        initGame();
    }

    public void loadImages() {

        ImageIcon iid = new ImageIcon(getClass().getResource("dot.png"));
        ball = iid.getImage();

        ImageIcon iia = new ImageIcon(getClass().getResource("apple.png"));
        apple = iia.getImage();

        ImageIcon iih = new ImageIcon(getClass().getResource("head.png"));
        head = iih.getImage();
        
        ImageIcon back = new ImageIcon(getClass().getResource("background2.png"));
        background = back.getImage();
        
        ImageIcon back1 = new ImageIcon(getClass().getResource("background.png"));
//        background = back1.getImage();

        ImageIcon memeBack = new ImageIcon(getClass().getResource("meme.png"));
        meme = memeBack.getImage();
        
        ImageIcon iiB = new ImageIcon(getClass().getResource("bomb.png"));
        bomb = iiB.getImage();

        
        
    }
    
   
    private void initGame() {

        dots = 3;

        for (int z = 0; z < dots; z++) {
            x[z] = 50 - z * 10;
            y[z] = 50;
        }
        
        locateApple();
        locateBomb();
//        checkLocation();

        timer = new Timer(DELAY, this);
        timer.start();
    }
    public void checkLocation() {

    	for(Bomb c : bombs) {
    		
    		if ((apple_x == c.bomb_x) && (apple_y == c.bomb_y)) {
            	
            	locateApple();
               
            }
    	}
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
            for(Bomb b : bombs) {
            	g.drawImage(bomb, b.bomb_x, b.bomb_y, this);

            }
            
            

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
    	
    	g.drawImage(meme, 250, 120, null);
    	
    	
    	
    	
    	
    	 
        
//        String msg = "Game Over";
//        Font small = new Font("Helvetica", Font.ITALIC, 130);
//        FontMetrics metr = getFontMetrics(small);
//
//        g.setColor(Color.white);
//        g.setFont(small);
//        g.drawString(msg, (B_WIDTH - metr.stringWidth(msg)) / 5, B_HEIGHT / 2);
        
        
        String msgB = "     Press Enter to        ";
        Font smallB = new Font("Helvetica", Font.ITALIC, 50);
        FontMetrics metrB = getFontMetrics(smallB);

        g.setColor(Color.white);
        g.setFont(smallB);
        g.drawString(msgB, (B_WIDTH - metrB.stringWidth(msgB)) / 30 * 2 /30 , B_HEIGHT * 2 / 3);
        
    
    }

    private void checkApple() {

        if ((x[0] == apple_x) && (y[0] == apple_y)) {

            dots++;
            score++;
            changeBackground();
            locateApple();
            isBomb = true;
//            locateBomb();
        }
        
        for(Bomb c : bombs) {
    		
    		if ((apple_x == c.bomb_x) && (apple_y == c.bomb_y)) {
            	
            	locateApple();
               
            }
    	}
    }
    
    private void checkBomb() {
    	
    	for(Bomb c : bombs) {
    		
    		if ((x[0] == c.bomb_x) && (y[0] == c.bomb_y)) {
            	
            	inGame = false;
               
            }
    	}
        
        
        if(score % 5 == 0 && isBomb == true) {
        	locateBomb();
        }
    }
    

    
    private void scoreBoard(Graphics g) {

    	 String msgA = "Current Score: " + score + "     ";
    	 Font smallA = new Font("Helvetica", Font.ITALIC, 20);
         FontMetrics metrA = getFontMetrics(smallA);

         g.setColor(Color.white);
         g.setFont(smallA);
         g.drawString(msgA, (B_WIDTH - metrA.stringWidth(msgA)) / 1 , B_HEIGHT / 10 );
         
         //timer doesnt work yet. 
//         String msgC = "Timer: " + timer.toString() + "     ";
//    	 Font smallC = new Font("Helvetica", Font.ITALIC, 20);
//         FontMetrics metrC = getFontMetrics(smallC);
//
//         g.setColor(Color.white);
//         g.setFont(smallC);
//         g.drawString(msgC, (B_WIDTH - metrC.stringWidth(msgC)) / 1 , B_HEIGHT / 2);
    	
    	
    }
    
    public void changeBackground() {
    	
    	if(score % 2 == 1) {
    		
    	} else if(score % 2 == 0) {
    		
    	}
    }
    
    public void restart() {

    	inGame = true;
    	initGame();
    	bombs.clear();
    	score = 0;
    	locateBomb();
    	
    	
    	rightDirection = true;
        upDirection = false;
        downDirection = false;
        leftDirection = false;

    	
    	
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

    private void locateBomb() {
    	isBomb = false;
    	int b = (int) (Math.random() * RAND_POS);
        int bomb_x = ((b * DOT_SIZE));

        b = (int) (Math.random() * RAND_POS);
        int bomb_y = ((b * DOT_SIZE));
        
        bombs.add(new Bomb(bomb_x,bomb_y));
        
    }
    
    @Override
    public void actionPerformed(ActionEvent e) {

        if (inGame) {

            checkApple();
            checkBomb();
            checkCollision();
            move();
        }

        repaint();
    }

    private class TAdapter extends KeyAdapter {

        @Override
        public void keyPressed(KeyEvent e) {

            int key = e.getKeyCode();

//            if ((key == KeyEvent.VK_LEFT) && (!rightDirection)) {
//                leftDirection = true;
//                upDirection = false;
//                downDirection = false;
//            }
//
//            if ((key == KeyEvent.VK_RIGHT) && (!leftDirection)) {
//                rightDirection = true;
//                upDirection = false;
//                downDirection = false;
//            }
//
//            if ((key == KeyEvent.VK_UP) && (!downDirection)) {
//                upDirection = true;
//                rightDirection = false;
//                leftDirection = false;
//            }

//            if ((key == KeyEvent.VK_DOWN) && (!upDirection)) {
//                downDirection = true;
//                rightDirection = false;
//                leftDirection = false;
//            }
//            
            
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
            if ((key == KeyEvent.VK_ENTER && (!inGame))) {
            	restart();
            	
            }
        }
    }
}