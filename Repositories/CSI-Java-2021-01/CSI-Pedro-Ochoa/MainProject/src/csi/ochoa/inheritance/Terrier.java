package csi.ochoa.inheritance;



public class Terrier extends Dog{

	public Terrier() {
		
		super("black", 30, false, false, "terrier.jpeg");
		
	}
	

	@Override
	public Noise bark(Noise n) {

		return new Noise(120, false);
	}
	
	
	public void wagTail() {
		
		System.out.println("Swish");
		
	}
	
	
}