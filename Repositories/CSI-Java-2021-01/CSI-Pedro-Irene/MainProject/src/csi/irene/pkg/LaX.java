package csi.irene.pkg;

import java.util.Arrays;

public class LaX {
	public static void main(String[] args) {

		int[][] arr = new int[10][10];

		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[i].length; j++) {
				
				arr [i][i] = 1 ; 
				arr [i][arr.length-1-i] = 1 ; 
				
				
				
				
				
				
				
				
				
				
				
				
		
			}
			System.out.println(Arrays.toString(arr[i]));
		}
	}

}
