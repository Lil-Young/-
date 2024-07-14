package java_algorithm;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		
		for(int t=1; t<T+1; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			
			int[][] arr = new int[N][N];
			
			for(int i=0; i<N; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j=0; j<N; j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			int max = 0;
			int Plustotal = 0, Multitotal = 0;
			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
					Plustotal = 0;
					Multitotal =0;
					Plustotal += arr[i][j];
					Multitotal += arr[i][j];
					for(int k=1; k<M; k++) {
						// + 방향, i-k, i+k, j-k, j+k
						if(i-k >= 0) {
							Plustotal += arr[i-k][j];
						}
						if(i+k < N) {
							Plustotal += arr[i+k][j];
						}
						if(j-k >= 0) {
							Plustotal += arr[i][j-k];
						}
						if(j+k < N) {
							Plustotal += arr[i][j+k];
						}
						
						// x 방향, (i-k,j-k), (i+k,j-k), (i-k, j+k), (i+k, j+k) 
						if(i-k >= 0 && j-k >= 0) {
							Multitotal += arr[i-k][j-k];
						}
						if(i+k < N && j-k >= 0) {
							Multitotal += arr[i+k][j-k];
						}
						if(i-k >= 0 && j+k < N) {
							Multitotal += arr[i-k][j+k];
						}
						if(i+k < N && j+k < N) {
							Multitotal += arr[i+k][j+k];
						}
						
						// max 갱신
						if(max < Plustotal) {
							max = Plustotal;
						}
						if(max < Multitotal) {
							max = Multitotal;
						}
					}

				}
			}
			System.out.println("#"+ t + " " + max);
		}
	}
}