# 파리 퇴치 / D2

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    
    result = 0
    limit = n-m
    x, y = 0, 0
    total = 0
    for i in range(m):
        for j in range(m):
            total += arr[i][j]
    if total > result:
        result = total
    if 