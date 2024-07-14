import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] arr = new int[10];
		int res = 0;
		int T = sc.nextInt();
		for(int i=1; i<T+1; i++) {
			res=0;
			for(int j=0; j<10; j++) {
				arr[j] = sc.nextInt();
				if(arr[j]>res) {
					res = arr[j];
				}
			}
			System.out.println("#"+i+" "+res);
		}
	}
}
