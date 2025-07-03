package csi.lopez.pkg;

import java.util.Arrays;

public class Loops {

	public Loops() {
		
	}

	public static void main(String[] args) {
		
//		for(int e = 0; e<10; e++) {
//			
//	    	System.out.println(e);
//	    }
//		
		
		int[][] arr = {
				{1,2,3,4,5},
				{5,6,7,8,9},
				{2,4,5,6,7}
				};
		
//		int[][] arr2= {{1,2,3,4,5}, {5,6,7,8,9}, {2,4,5,6,7}};
		
//		System.out.print(Arrays.toString( arr[0] ));
		
		nestedPrint(arr);
		
	}
	
	public static void nestedPrint(int[][] arr) {
		for(int i=0; i <arr.length; i++) {
			for(int j=0; j< arr[i].length; j++) {
				System.out.println( arr[i][j]);
			}
		}
	}
}
