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
			String[][] arr = new String[N][N];
			for(int i=0; i<N; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j=0; j<N; j++) {
					arr[i][j] = st.nextToken();
				}
			}
			String[][] result = new String[N][3];
			
			
			String a = "";
			// 90도
			int cnt = 0;
			for(int i=0; i < N; i++) {
				a = "";
				for(int j=N-1; j>=0; j--) {
					a+=arr[j][i];
				}
				result[cnt][0] = a;
				cnt++;
			}
			
			// 180도
			a = "";
			cnt = 0;
			for(int i=N-1; i>=0; i--) {
				a ="";
				for(int j=N-1; j>=0; j--) {
					a+=arr[i][j];
				}
				result[cnt][1] = a;
				cnt++;
			}
						
			// 270도
			a = "";
			cnt = 0;
			for(int i=N-1; i>=0; i--) {
				a = "";
				for(int j=0; j < N; j++) {
					a+=arr[j][i];				}
				result[cnt][2] = a;
				cnt++;
			}
			
			System.out.println("#" + t + " ");
			for(String[] re : result) {
				for(int i=0; i<3; i++) {
					System.out.print(re[i]);
					if(i!=N-1) {
						System.out.print(" ");
					}
				}
				System.out.println();
			}
		}
	}
}