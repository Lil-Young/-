package java_algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Solution {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] n = br.readLine().split(" ");
		int end = Integer.parseInt(n[0]);
		int start = Integer.parseInt(n[1]);
		int result = Math.abs(end-start)+1;
		System.out.println(result);
	}
}