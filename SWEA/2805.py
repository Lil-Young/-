# 농작물 수확하기 / D3

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input())))
    index = n//2
    index1, index2 = index-1, index+1
    total = sum(graph[index])
    for i in range(1, index+1):
        total+=sum(graph[index1][i:n-i])
        total+=sum(graph[index2][i:n-i])
        index1-=1
        index2+=1
    print(f"#{tc} {total}")