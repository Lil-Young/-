N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

def dfs(x, y):
    if x >= N or y >= N or graph[x][y] == 0:
        return False
    if graph[x][y] == -1:
        return True
    
    if dfs(x, y+graph[x][y]) == True or dfs(x+graph[x][y], y) == True:
        return True
    
        
if dfs(0, 0) == True:
    print("HaruHaru")
else:
    print("Hing")