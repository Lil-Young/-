package java_algorithm;

import java.util.Arrays;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
	    int[] months = new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
	    int[] days = new int[] {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
		int T = sc.nextInt();
		sc.nextLine();
		for(int tc=0; tc<T; tc++) {
			String y="", m="", d="";
			String input = sc.nextLine();
			String[] arr = input.split("");
			for(int i=0; i<arr.length; i++) {
				if(i<4) {
					y+=arr[i];
				}else if (i >= 4 && i < 6) {
					m+=arr[i];
				}else {
					d+=arr[i];
				}
			}
			// m과 d의 데이터 타입을 String에서 int로 변경
			int a = Integer.parseInt(m);
			int b = Integer.parseInt(d);
			// 정수 a가 months 배열에 포함되어있는지 확인.
			boolean contain = Arrays.stream(months).anyMatch(num -> num == a);
			if(contain && (b > 0 && b <= days[a-1])) {
				System.out.println("#" + (tc+1) + " " + y + "/" + m + "/" + d);
			}else {
				System.out.println("#" + (tc+1) + " " +-1);
			}
		}
	}

}
