package csi.lopez.pkg;

import java.util.Arrays;

public class LaX3D {

	public LaX3D() {
		// TODO Auto-generated constructor stub
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		int[][][] arr = new int[2][9][9];

//		for(int i = 0;i<arr.length;i++) {
//			System.out.println("--------------------------------");
//			
//			for(int j = 0; j < arr[i].length; j++) {
//				
//			    for(int k = 0; k < arr[i][j].length; k++) {
//	
//			    	arr[i][j][j] = 1;
//			    	arr[i][j][ arr[i][j].length - j - 1 ] = 1;
//			    }
//			    System.out.println(Arrays.toString(arr[i][j]));
//			    
//			}
//			
//			System.out.println("--------------------------------");
//			for (int j = 0; j < arr[1].length; j++) {
//			  for (int k = 0; k < arr[1][j].length; k++) {
//				  
//				  arr[i][j][k] = 1;
//				  arr[i][j][j] = 0;
//				  arr[i][j][arr[i][j].length - j - 1 ] = 0;
//				  
//			  }
//			  System.out.println(Arrays.toString(arr[1][j]));
//			}
//			
//		}
//		
//		
//	}
		int[][][] arr = new int[2][9][9];

		System.out.println("--------------------------------");
		for (int j = 0; j < arr[0].length; j++) {
		  for (int k = 0; k < arr[0][j].length; k++) {

			  arr[0][j][j] = 1;
			  arr[0][j][ arr[0][j].length - j - 1 ] = 1;

		  }
		  System.out.println(Arrays.toString(arr[0][j]));

		}

		System.out.println("--------------------------------");
		for (int j = 0; j < arr[1].length; j++) {
		  for (int k = 0; k < arr[1][j].length; k++) {
			  
//			  arr[1][j][k] = 1; 
//			  arr[1][j][j] = 0; 
//			  arr[1][j][ arr[1][j].length - j - 1 ] = 0;		  

			  arr[1][j][k] = 1 - arr[0][j][k];

		  }
		  System.out.println(Arrays.toString(arr[1][j]));
		}
		
		
	
		
	}

}
