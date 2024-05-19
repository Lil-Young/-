# 회문1 / D3

for tc in range(1, 11):
    t = int(input())
    graph = []
    for _ in range(8):
        graph.append(list(input()))
    r_graph = []
    for i in range(8):
        arr = []
        for j in range(8):
            arr.append(graph[j][i])
        r_graph.append(arr)

    total = 0
    for s1, s2 in zip(graph, r_graph):
        for j in range(8):
            if j+t > 8:
                break
            word1 = s1[j:j+t]
            word2 = s2[j:j+t]
            if word1 == list(reversed(word1)):
                total+=1
            if word2 == list(reversed(word2)):
                total+=1
    print(f"#{tc} {total}")