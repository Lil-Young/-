package java_algorithm;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Solution {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] arr = br.readLine().split(" ");
		int a = Integer.parseInt(arr[0]), b = Integer.parseInt(arr[1]);
		if((a==1&&b==3) || (a==2&&b==1) || (a==3&&b==2)) {
			System.out.println('A');
		}else {
			System.out.println('B');
		}
	}
}