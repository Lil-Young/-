package java_algorithm;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Solution {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String a = br.readLine();
		int N = Integer.parseInt(a);
		for(int i=1; i<N+1; i++) {
			if(N%i==0) {
				if(i!=N) {
					System.out.print(i + " ");
				}else {
					System.out.print(i);
				}
			}
		}
		
	}
}