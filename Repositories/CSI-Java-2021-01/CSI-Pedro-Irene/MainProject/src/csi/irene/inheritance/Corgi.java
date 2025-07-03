package csi.irene.inheritance;

public class Corgi extends Dog {

		public Corgi() {
			
			super("black", 15, false, true, "MediumCorgi.png");
			
		}
		
		@Override
		
		public Noise Bark() {

			return new Noise(50, false);
		}
		
		
		public void wagTail() {
			
			System.out.println("small swish");
			
		}
		
		public Shit eat() {

			return new Shit(true, 2, "cheeto");
		}
	}

