n, m, v = map(int, input().split())
# graph = [[]]
# for _ in range(m):
#     graph.append(list(map(int, input().split())))
# visited = [False] * (n+1)
# print(n, m, v)
# print(graph)
# print(visited)

# def dfs(v):
#     visited[v] = True
#     print(v, end=" ")
#     for i in graph[v]:
#         if not visited[i] and i in graph[i]:
#             dfs(i)

# dfs(v)


from collections import defaultdict
graph = defaultdict(str, list)
for _ in range(m):
    key, value = input().split()
    graph[key].append(value)
print(graph)