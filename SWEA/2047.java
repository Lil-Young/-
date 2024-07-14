package java_algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Solution {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] arr = br.readLine().split("");
		for(int i=0; i<arr.length; i++) {
			arr[i] = arr[i].toUpperCase();
		}
		String str = String.join("", arr);
		System.out.print(str);
	}
}