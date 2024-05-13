# N은 가로 크기, M은 세로 크기
N, M = map(int, input().split())
graph = []
for _ in range(M):
    graph.append(list(map(int, input().split())))
visited = [[False] * N for _ in range(M)]
visited[0][0] = True
dx = [0, 1]
dy = [1, 0]
