# Magnetic / D3

for tc in range(1, 11):
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    result = 0
    for i in range(n):
        stack = []
        for j in range(n):
            if not stack and graph[j][i] == 1:
                stack.append(1)
            elif stack and graph[j][i] == 2:
                stack.pop()
                result+=1
    print(f"#{tc} {result}")