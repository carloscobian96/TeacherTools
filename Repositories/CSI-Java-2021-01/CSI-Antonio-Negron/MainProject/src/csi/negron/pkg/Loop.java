package csi.negron.pkg;

import java.util.Arrays;

public class Loop {

	public static void main(String[] args) {

//	for (int i = 0; i < 10; i++) {
//
//		System.out.println(i);
//
//		}

		// int[][] arr = new int[3][5];
		// arr[0][0]=1;
		// System.out.println("arr[0][0]=");

		int[][] arr2 = { { 19, 11, 20, 15, 40 }, { 13, 26, 50, 8, 66 }, { 76, 54, 33, 80, 56 } };
//		arr2[0][0] = 1;
//		System.out.println(Arrays.toString(arr2[0]));
        nestedPrint(arr2);
	}

	public static void nestedPrint(int[][] arr2) {

		for (int i = 0; i < arr2.length; i++) {
			for (int j = 0; j < arr2[i].length; j++){
				System.out.println(arr2[i][j]);
			}
		}
	}

}
