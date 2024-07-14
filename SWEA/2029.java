package java_algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Solution {

	public static void main(String[] args) throws IOException {
		// 2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String T = br.readLine();
		int t = Integer.parseInt(T);
		for(int i=0; i<t; i++) {
			String[] arr = br.readLine().split(" ");
			int a = Integer.parseInt(arr[0]), b = Integer.parseInt(arr[1]);
			
			System.out.println("#"+(i+1) + " " + a/b + " " + a%b);
		}
	}
}