package java_algorithm;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 상호의_배틀필드_1873 {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		// test_case
		int T = Integer.parseInt(br.readLine());
		for(int t=1; t<T+1; t++) {
		
			// 입력 받기
			StringTokenizer st = new StringTokenizer(br.readLine());
			int H = Integer.parseInt(st.nextToken());
			int W = Integer.parseInt(st.nextToken());
			String[][] map = new String[H][W];
			int a=0, b=0;
			for (int i = 0; i < H; i++) {
				String str = br.readLine();
				for (int j = 0; j < W; j++) {
					map[i][j] = Character.toString(str.charAt(j));
					// 전차 위치(a, b)
					if(map[i][j].equals("^") || map[i][j].equals("v") || map[i][j].equals("<") || map[i][j].equals(">")) {
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
			int n = Integer.parseInt(br.readLine());
			String str2 = br.readLine();
			for(int q=0; q<n; q++) {
				String input = Character.toString(str2.charAt(q));
				int[] dr = {-1, 1, 0, 0};
				int[] dc = {0, 0, -1, 1};
				if(input.equals("U")) {
					int nr = a+dr[0];
					int nc = b+dc[0];
					d = "^";
					if(nr >= 0 && map[nr][nc].equals(".")) {
						map[a][b] = ".";
						a = nr;
						b = nc;
					}
				}else if(input.equals("D")) {
					int nr = a+dr[1];
					int nc = b+dc[1];
					d = "v";
					if(nr < H && map[nr][nc].equals(".")) {
						map[a][b] = ".";
						a = nr;
						b = nc;
					}
				}else if(input.equals("L")) {
					int nr = a+dr[2];
					int nc = b+dc[2];
					d = "<";
					if(nc >= 0 && map[nr][nc].equals(".")) {
						map[a][b] = ".";
						a = nr;
						b = nc;
					}
				}else if(input.equals("R")) {
					int nr = a+dr[3];
					int nc = b+dc[3];
					d = ">";
					if(nc < W && map[nr][nc].equals(".")) {
						map[a][b] = ".";
						a = nr;
						b = nc;
					}
				}else if(input.equals("S")) {
					int lanuch = -1;
					int range = 0;
					if(d.equals("^")) {
						lanuch = 0;
						range = H;
					}else if(d.equals("v")) {
						lanuch = 1;
						range = H;
					}else if(d.equals("<")) {
						lanuch = 2;
						range = W;
					}else if(d.equals(">")){
						lanuch = 3;
						range = W;
					}
					int dx = a;
					int dy = b;
					int nx = dx+dr[lanuch];
					int ny = dy+dc[lanuch];
					for(int k=0; k<range; k++){
						if(nx>=0 && nx<H && ny>=0 && ny<W) {
							if(map[nx][ny].equals("*")) {
								map[nx][ny] = ".";
								break;
							}else if(map[nx][ny].equals("#")) {
								break;
							}else {
								nx = nx+dr[lanuch];
								ny = ny+dc[lanuch];
							}
						}else {
							break;
						}
					}
				}
			}
			map[a][b] = d;
			System.out.print("#"+t+" ");
			for(int i=0; i<H; i++) {
				for(int j=0; j<W; j++) {
					System.out.print(map[i][j]);
				}
				System.out.println();
			}
		}
		
	}

}
