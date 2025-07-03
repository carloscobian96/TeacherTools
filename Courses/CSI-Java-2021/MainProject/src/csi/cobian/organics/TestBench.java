package csi.cobian.organics;

import java.util.Arrays;

public class TestBench {

	public static void main(String[] args) {
		int[][][] arr = new int[2][9][9];
		for(int i = 0; i < arr.length; i++) {
			for(int j = 0; j < arr[i].length; j++) {
				for(int k = 0; k < arr[i].length; k++) {
					arr[i][j][j] = 1;
					arr[i];
				}
	}

  }
 }
}







//package csi.cobian.organics;
//
//import java.util.Arrays;
//
//import csi.cobian.organics.taxonomy.archaea.Archaea;
//import csi.cobian.organics.taxonomy.bacteria.Bacteria;
//import csi.cobian.organics.taxonomy.eukarya.Eukarya;
//
//public class TestBench {
//
//	public static void main(String[] args) {
//		
//				
////		Domain[] myDomains = new Domain[] { new Eukarya(), new Bacteria() , null};
//		
//		Organism[] myOrganisms = new Organism[] { new Eukarya(), new Bacteria() , null};
//		
//		myOrganisms[2]= new Archaea();
//		System.out.println(myOrganisms[2].getClass());
//		
//		Class<?> var = myOrganisms[2].getClass();
//		System.out.println("\n---------------------------");
//		System.out.println("----Let there be light!----");
//		System.out.println("---------------------------\n");
//		
////		Arrays.stream(myOrganisms).forEach(n -> 
////			{	System.out.println("---------------------------");
////				System.out.println(n);
////				System.out.println(n.name + " Says:");
////				n.requestFood();
////				n.reproduce();
////				System.out.println("---------------------------\n");
////			});
//		
//		
//	}
//}
