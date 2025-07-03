package csi.quiros.inheritance;


public class Greyhound extends Dog{

	public Greyhound() {
		
		super("Blue Brindle", 40, false, false, "GreyHound.png");

	}

	public Noise bark() {

		return new Noise(100, false);
	}
	
	
	public void wagTail() {
		
		System.out.println("Im wagging!");
		
	}
	
	public Shit eat() {

		return new Shit(true, 3, "Poopy");
	}
}


//   20/20 plz