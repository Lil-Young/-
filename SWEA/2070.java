import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner scanner = new Scanner(System.in);
		int T = scanner.nextInt();
		int[] arr = new int[2];
		for(int t=1; t<T+1; t++) {
			for(int j=0; j<2; j++) {
				arr[j] = scanner.nextInt();
			}
			if(arr[0] > arr[1]) {
				System.out.println("#"+t+" "+">");
			}else if(arr[0] < arr[1]) {
				System.out.println("#"+t+" "+"<");
			}else {
				System.out.println("#"+t+" "+"=");
			}
		}
	}
}