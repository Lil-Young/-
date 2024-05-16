# 어디에 단어가 들어갈 수 있을까 / D2

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    # 1이 흰색(안막힌 부분), 0이 검은색(막힌 부분)
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    
    total = 0
    for x in range(n):
        x_cnt = 0
        y_cnt = 0
        for y in range(n):
            if arr[x][y] == 0:
                if y_cnt == k:
                    total += 1
                y_cnt = 0
            else:
                y_cnt += 1

            if arr[y][x] == 0:
                if x_cnt == k:
                    total += 1
                x_cnt = 0
            else:
                x_cnt += 1

        if y_cnt == k:
            total += 1
        if x_cnt == k:
            total += 1
            
    print(f"#{tc} {total}")