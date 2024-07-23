// D3 / 햄버거 다이어트
package java_algorithm;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.text.ParseException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;
import java.util.StringTokenizer;

public class Solution {
    static ArrayList<int[]> list;
    static int N;
    static int L;

    static int result = 0;

    private static void recursive(int idx, int score, int cal) {

        if(cal > L) {
            return;
        }
        if(score > result) {
            result = score;
        }
        if(idx >= N) {
        	return;
        }

        score += list.get(idx)[0];
        cal += list.get(idx)[1];
        // 선택
        recursive(idx+1, score, cal);

        score -= list.get(idx)[0];
        cal -= list.get(idx)[1];
        // 선택x
        recursive(idx+1, score, cal);

    }




    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int TC = Integer.parseInt(br.readLine());
        for (int t = 1; t < TC+1; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            // N: 재료의 수, L: 제한 칼로리
            N = Integer.parseInt(st.nextToken());
            L = Integer.parseInt(st.nextToken());
            list = new ArrayList<>();
            for(int i=0; i<N; i++) {
                st = new StringTokenizer(br.readLine());
                // T: 점수, K: 칼로리
                int[] arr = new int[2];
                int T = Integer.parseInt(st.nextToken());
                int K = Integer.parseInt(st.nextToken());
                arr[0] = T;
                arr[1] = K;
                list.add(arr);

            }
        // 주어진 제한 칼로리 이하의 조합중에서 가장 맛에 대한 점수가 높은 햄버거의 점수 출력        
            result = 0;
            recursive(0, 0, 0);
        
        
        
//1
//5 1000
//100 200
//300 500
//250 300
//500 1000
//400 400
        


            System.out.println("#"+t+" "+result);
        }
    }
}