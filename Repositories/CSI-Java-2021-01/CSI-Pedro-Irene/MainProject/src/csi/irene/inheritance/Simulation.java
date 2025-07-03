package csi.irene.inheritance;
import java.awt.EventQueue;
import javax.swing.JFrame;

public class Simulation extends JFrame {

	public Simulation() {

		initUI();
	}

	private void initUI() {

		add(new Dogpound());

		setResizable(false);
		pack();

		setTitle("Dogpound");
		setLocationRelativeTo(null);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
	
        
	}


	public static void main(String[] args) {

		EventQueue.invokeLater(() -> {
			JFrame ex = new Simulation();
			ex.setVisible(true);
		});
	}
}


	
	
	
	
	

