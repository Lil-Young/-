# N은 가로 크기, M은 세로 크기
N, M = map(int, input().split())
graph = []
for _ in range(M):
    graph.append(list(map(int, input().split())))
visited = [[False] * N for _ in range(M)]
visited[0][0] = True
dx = [0, 1]
dy = [1, 0]

def dfs(x, y):

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < M and ny >= 0 and ny < N and not visited[nx][ny] and graph[nx][ny] == 1:
            visited[nx][ny] = True
            dfs(nx, ny)
                
dfs(0, 0)
if visited[M-1][N-1]:
    print("Yes")
else:
    print("No")