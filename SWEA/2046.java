package java_algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Solution {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String num = br.readLine();
		int n = Integer.parseInt(num);
		String s = "";
		for(int i=0; i<n; i++) {
			s+="#";
		}
		System.out.println(s);
	}
}