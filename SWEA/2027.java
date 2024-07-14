package java_algorithm;

import java.io.IOException;

public class Solution {

	public static void main(String[] args) throws IOException {
		String s = "#", p = "+";
		String[] arr = new String[] {"+", "+", "+", "+", "+"};
		for(int i=0; i<5; i++) {
			arr[i] = s;
			System.out.println(String.join("", arr));
			arr[i] = p;
		}
	}
}