package java_algorithm;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

class Cal{
	int a, b;
	
	public int sum(int a, int b) {
		return a+b;
	}
	public int minus(int a, int b) {
		return a-b;
	}
	public int multi(int a, int b) {
		return a*b;
	}
	public int divide(int a, int b) {
		return a/b;
	}
}

public class Solution {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] arr = br.readLine().split(" ");
		int a = Integer.parseInt(arr[0]), b = Integer.parseInt(arr[1]);
		Cal obj = new Cal();
		System.out.println(obj.sum(a, b));
		System.out.println(obj.minus(a, b));
		System.out.println(obj.multi(a, b));
		System.out.println(obj.divide(a, b));
		
	}
}