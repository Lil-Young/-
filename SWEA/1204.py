# 최빈수 구하기 / D2

from collections import defaultdict

T = int(input())
for tc in range(1, T+1):
    t = int(input())
    a = list(map(int, input().split()))
    dic = defaultdict(int)
    for i in a:
        dic[i] += 1
    max_num = max(dic.values())
    result = []
    for d in dic.items():
        if d[1] == max_num:
            result.append(d[0])
    result.sort(reverse=True)
    print(f"#{tc} {result[0]}")