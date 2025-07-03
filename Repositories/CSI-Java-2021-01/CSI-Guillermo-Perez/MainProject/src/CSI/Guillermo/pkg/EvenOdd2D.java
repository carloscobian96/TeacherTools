/**
 * 
 */
package csi.guillermo.pkg;

import java.util.Arrays;

/**
 * @author guillermoperez
 *
 */
public class EvenOdd2D {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		//Main Method
		int[][] arr = new int[10][10];

		for(int i = 0; i < arr.length; i++) {
		    for(int j = 0; j < arr[i].length; j++) {
		    
		    	if(i % 2 == 1) {
		    		if(j % 2 == 1) {
		    			arr[i][j]=1;
		    		}
		    	} else {
		    		if(j % 2 == 0) {
		    			arr[i][j]=1;
		    	
		    }
		    	}
		    }
		    System.out.println(Arrays.toString(arr[i]));
		}
	}
}
