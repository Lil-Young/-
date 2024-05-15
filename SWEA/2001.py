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
    while x <= limit:
        total = 0
        for i in range(x, m+x):
            for j in range(y, m+y):
                total += arr[i][j]
        if total > result:
            result = total
        y+=1
        if y > limit:
            x+=1
            y = 0
    print(f"#{test_case} {result}")