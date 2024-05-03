import sys
input = sys.stdin.readline

graph = []
for _ in range(5):
    graph.append(list(map(int, input().split())))
visited = [[False] * 5 for _ in range(5)]
x, y = map(int, input().split())
nx = [-1, 1, 0, 0]
ny = [0, 0, -1, 1]

# 1이면 사과, 0이면 없음, -1이면 벽
def dfs(x, y, depth, apple):
    if graph[x][y] == 1:
        apple += 1
    if depth == 3:
        if apple >= 2:
            return True
        return
    for i in range(4):
        dx = x + nx[i]
        dy = y + ny[i]
        if dx < 0 or dx >= 5 or dy < 0 or dy >= 5 or graph[dx][dy] == -1:
            continue
        graph[x][y] = -1
        if dfs(dx, dy, depth + 1, apple):
            return True
        graph[x][y] = 0 

if dfs(x, y, 0, 0):
    print(1)
else:
    print(0)