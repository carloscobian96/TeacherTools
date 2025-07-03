package csi.lopez.pkg;

import java.util.Arrays;

public class LaX {

	public LaX() {
		// TODO Auto-generated constructor stub
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int[][] arr = new int[9][9];
		
		
		crearX(arr);
	}
	public static void crearX(int[][] arr) {
		
		for(int i = 0; i < arr.length; i++) {
		    for(int j = 0; j < arr[i].length; j++) {
		    	
		    	arr[i][j] = 1;
		    	arr[j][j] = 0;
		    	arr[j][arr.length - j - 1] = 0;
		    	
		    	
		    	
		    	
		    } 
		    
		    System.out.println(Arrays.toString(arr[i]));
		}
		
		 
	}
	
	

}
