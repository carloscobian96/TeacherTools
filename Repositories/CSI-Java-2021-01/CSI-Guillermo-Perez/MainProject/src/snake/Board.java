package snake;

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

import csi.perez.finance.Loan;

public class Board extends JPanel implements ActionListener {

	
	
    private final int B_WIDTH = 1000;
    private final int B_HEIGHT = 750;
    private final int DOT_SIZE = 50;
    private final int ALL_DOTS = 1000;
    private final int RAND_POS = 10;
    private final int DELAY = 140;
     
    
    private final int x[] = new int[ALL_DOTS];
    private final int y[] = new int[ALL_DOTS];

    private int score = 0;
    
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

    private Timer timer;
    private Image ball;
    private Image apple;
    private Image head;
    private Image background;
    private Image mine;
    
    
//    private Image background;

    public Board() {
        
        initBoard();
    }
    
    private void initBoard() {

        addKeyListener(new TAdapter());
        setFocusable(true);

        setPreferredSize(new Dimension(B_WIDTH, B_HEIGHT));
        loadImages();
        initGame();
    }

    private void loadImages() {
//
    	ImageIcon iid = new ImageIcon(getClass().getResource("dot.png"));
        ball = iid.getImage();

        ImageIcon iia = new ImageIcon(getClass().getResource("ender.png"));
        apple = iia.getImage();
        
        ImageIcon iih = new ImageIcon(getClass().getResource("steve.png"));
        head = iih.getImage();
        
        ImageIcon iig = new ImageIcon(getClass().getResource("end.png"));
        background = iig.getImage();
        
        ImageIcon iim = new ImageIcon(getClass().getResource("mine.png"));
        mine= iim.getImage();
    }

    private void initGame() {

        dots = 1;

        for (int z = 0; z < dots; z++) {
            x[z] = 50 - z * 10;
            y[z] = 50;
        }
        
        locateApple();

        timer = new Timer(DELAY, this);
        timer.start();
    }

    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);

        doDrawing(g);
    }
    
    private void doDrawing(Graphics g) {
        
        if (inGame) {
      
        	g.drawImage(background, 0, 0, null);
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

        
        String msg = "Game Over";
        Font small = new Font("Helvetica", Font.BOLD, 24);
        FontMetrics metr = getFontMetrics(small);

        Random color = new Random();

        
        int r = color.nextInt(255);
        int n = color.nextInt(255);
        int b = color.nextInt(255);
       
        g.setColor(new Color(r,n,b));
        g.setFont(small);
        g.drawString(msg, (B_WIDTH - metr.stringWidth(msg)) / 2, B_HEIGHT / 2);
        
        
        String msgB = "																								Enter = Restart";
        Font smallB = new Font("Helvetica", Font.ITALIC, 50);
        FontMetrics metrB = getFontMetrics(smallB);
        
        g.setColor(new Color(r,n,b));
        g.setFont(smallB);
        g.drawString(msgB, (B_WIDTH - metr.stringWidth(msgB)) / 30 * 2 /30 , B_HEIGHT * 2 / 3);
    }

    
    private void checkApple() {



        if ((x[0] == apple_x) && (y[0] == apple_y)) {
        	
            dots++;
            score++;
            locateApple();
         
            Random color = new Random();
           
        
            int r = color.nextInt(255);
            int n = color.nextInt(255);
            int b = color.nextInt(255);
           
            setBackground(new Color(r,n,b));
//         


        }
    }
    
    private void checkMine() {

    	if ((x[0] == mine_x) && (y[0] == mine_y)) {
        	
            score-=dots;
            locateMine();
            if(score < 1) {
            		inGame = false;
}
    }
    }
    
    private void scoreBoard(Graphics g) {

   	 String msgA = "Current Score: " + score + "     ";
   	 Font smallA = new Font("Helvetica", Font.BOLD, 20);
        FontMetrics metrA = getFontMetrics(smallA);

        Random color = new Random();

        
        int r = color.nextInt(255);
        int n = color.nextInt(255);
        int b = color.nextInt(255);
        
        g.setColor(new Color(r,n,b));
        g.setFont(smallA);
        g.drawString(msgA, (B_WIDTH - metrA.stringWidth(msgA)) / 1 , B_HEIGHT / 15 );
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
    
    public void actionPerformed(ActionEvent e) {

        if (inGame) {

        	checkMine();
            checkApple();
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
            	 if (!inGame) {
                     timer.stop();
                 }
            	restart();
            	
            }
            
        }
    }
}

