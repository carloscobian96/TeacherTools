/**
 * 
 */
package csi.guillermo.pkg;

import java.util.Arrays;

/**
 * @author guillermoperez
 *
 */
public class LaX {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
//Main Method

	int[][] arr = new int[9][9];

	for(int i = 0; i < arr.length; i++) {
	    for(int j = 0; j < arr[i].length; j++) {
	      arr[i][i]=1;
	      arr[i][arr[i].length - i - 1 ]=1;
	    }
	    System.out.println(Arrays.toString(arr[i]));
	}
	}
}
