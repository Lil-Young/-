package java_algorithm;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int t=1; t<T+1; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			
			int[] A = new int[N];
			int[] B = new int[M];
			st = new StringTokenizer(br.readLine());
			for(int i=0; i<N; i++) {
				A[i] = Integer.parseInt(st.nextToken());
			}
			st = new StringTokenizer(br.readLine());
			for(int i=0; i<M; i++) {
				B[i] = Integer.parseInt(st.nextToken());
			}
			if(A.length > B.length) {
				int[] temp = A;
				A = B;
				B = temp;
			}
			int k = 0;
			int total = 0;
			int result = 0;
			for(int i=0; i<(B.length-A.length)+1; i++) {
				k = 0;
				total = 0;
				for(int j=i; j<i+A.length; j++) {
					total += (A[k]*B[j]);
					k++;
				}
				if(total > result) {
					result = total;
				}
			}
			System.out.println("#" + t + " " + result);
		}
	}
}