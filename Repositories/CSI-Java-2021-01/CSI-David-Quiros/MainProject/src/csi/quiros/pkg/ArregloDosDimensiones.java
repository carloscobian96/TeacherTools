package csi.quiros.pkg;

import java.util.Arrays;

public class ArregloDosDimensiones {

	public static void main(String[] args) {
		
		int[][] arr = {
				{1,2,3,4,5},
				{6,7,8,9,10},
				{11,12,13,14,15}
				};
		
		//System.out.println( arr[2][4]);
		//System.out.println(Arrays.toString( arr[0]));
		
		nestedPrint(arr);
	}

	
	
	public static void nestedPrint(int[][] arr) {
		
		for(int i = 0; i < arr.length; i++) {
		//System.out.println(Arrays.toString( arr[i]));
			for(int j = 0; j < arr[i].length; j++) {
			System.out.println(arr[i][j]);
			
			}
		}
	}
}