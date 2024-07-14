import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String input = sc.next();
		int sum = 0;
		char[] arr = input.toCharArray();
		for(int i=0; i<arr.length; i++) {
			sum += Character.getNumericValue(arr[i]);
		}
		System.out.println(sum);
	}
}