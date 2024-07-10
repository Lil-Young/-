import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		int arr[] = new int[10];
		Scanner scanner = new Scanner(System.in);
		int total=0;
		double avg;
		int T = scanner.nextInt();
		for(int t=1; t<T+1; t++) {
			total = 0;
			for(int i=0; i<10; i++) {
				arr[i] = scanner.nextInt();
				total += arr[i];
			}
			avg = Math.round((double) total/10);
			System.out.println("#"+t+" "+(int) avg);
		}
	}
}