package java_algorithm;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 상호의_배틀필드_1873 {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		// test_case
		int T = Integer.parseInt(br.readLine());
		
		// 입력 받기
		StringTokenizer st = new StringTokenizer(br.readLine());
		int H = Integer.parseInt(st.nextToken());
		int W = Integer.parseInt(st.nextToken());
		String[][] map = new String[H][W];
		int a=0, b=0;
		for (int i = 0; i < H; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < W; j++) {
				map[i][j] = st.nextToken();
				// 전차 위치(a, b)
				if(map[i][j].equals("<") || map[i][j].equals("v") || map[i][j].equals("<") || map[i][j].equals(">")) {
					a = i;
					b = j;
				}
			}
		}
		
		/*
		 * . 평지 / * 벽돌 / # 강철 / - 물 / ^ 위쪽바라봄 / v 아래쪽바라봄 / < 왼쪽바라봄 / > 오른쪽바라봄
		 * U 위 칸이 평지면 위로 이동
		 * D 아래 칸이 평지면 아래로 이동
		 * L 왼쪽 칸이 평지면 왼쪽으로 이동
		 * R 오른쪽 칸이 평지면 오른쪽으로 이동
		 * S 전차가 현재 바라보고 있는 방향으로 포탄 발사
		 */
		String d = map[a][b];
		st = new StringTokenizer(br.readLine());
		while(st.hasMoreTokens()) {
			String input = st.nextToken();
			int[] dr = {-1, 1, 0, 0};
			int[] dc = {0, 0, -1, 1};
			if(input.equals("U")) {
				int nr = a+dr[0];
				int nc = b+dc[0];
				if(nr >= 0 && map[nr][nc].equals(".")) {
					map[a][b] = ".";
					a = nr;
					d = "^";
				}
			}else if(input.equals("D")) {
				int nr = a+dr[1];
				int nc = b+dc[1];
				if(nr < H && map[nr][nc].equals(".")) {
					map[a][b] = ".";
					a = nr;
					d = "v";
				}
			}else if(input.equals("L")) {
				int nr = a+dr[2];
				int nc = b+dc[2];
				if(nc >= 0 && map[nr][nc].equals(".")) {
					map[a][b] = ".";
					b = nc;
					d = "<";
				}
			}else if(input.equals("R")) {
				int nr = a+dr[3];
				int nc = b+dc[3];
				if(nc < W && map[nr][nc].equals(".")) {
					map[a][b] = ".";
					b = nc;
					d = ">";
				}
			}else if(input.equals("S")) {
				
			}
		}
		
	}

}
