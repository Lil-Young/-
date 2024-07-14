package java_algorithm;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Solution {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String a = br.readLine();
		int b = Integer.parseInt(a);
		for(int i=b; i>=0; i--) {
			if(i!=0) {
				System.out.print(i + " ");
			}
			else {
				System.out.print(i);
			}
		}
	}
}