def dfs1(x, y):
    if x >= n or y >= m:
        return
    if visited[x][y] == 0 and graph[x][y] == '-':
        visited[x][y] = 1
        dfs1(x, y+1)
        return True
    return False

def dfs2(x, y):
    if x >= n or y >= m:
        return
    if visited[x][y] == 0 and graph[x][y] == '|':
        visited[x][y] = 1
        dfs2(x+1, y)
        return True
    return False

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(input()))

visited = [[0]*m for _ in range(n)]

result = 0
for i in range(n):
    for j in range(m):
        if dfs1(i, j) == True or dfs2(i, j) == True:
            result += 1
print(result)
print(graph)
print(visited)