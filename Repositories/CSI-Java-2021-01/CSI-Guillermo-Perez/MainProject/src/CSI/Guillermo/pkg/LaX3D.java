/**
 * 
 */
package csi.guillermo.pkg;

import java.util.Arrays;

/**
 * @author guillermoperez
 *
 */
public class LaX3D {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		// Main method
		int[][][] arr = new int[2][9][9];

		System.out.println("--------------------------------");
		for (int j = 0; j < arr[0].length; j++) {
			for (int k = 0; k < arr[0][j].length; k++) {
				arr[0][j][j] = 1;
				arr[0][j][arr[0].length - j - 1] = 1;
				
			}
			System.out.println(Arrays.toString(arr[0][j]));

		}

		System.out.println("--------------------------------");
		for (int j = 0; j < arr[1].length; j++) {
			for (int k = 0; k < arr[1][j].length; k++) {

				arr[1][j][k] = 1 - arr[0][j][k];
		

			}
			System.out.println(Arrays.toString(arr[1][j]));
		}

	}

}
