package java_algorithm;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Solution {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String a = br.readLine();
		int b = Integer.parseInt(a);
		int re = 1;
		for(int i=0; i<b+1; i++) {
			if(i!=b) {
				System.out.print(re + " ");
				re *= 2;
			}else {
				System.out.print(re);
			}
		}
	}
}