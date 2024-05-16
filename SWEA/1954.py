# 달팽이 숫자 / D2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    num = 1
    x, y = 0, 0
    pos = "R"
    while num != N**2+1:
        if pos == "R":
            arr[x][y] = num
            y+=1
            if y == N or arr[x][y] != 0:
                pos = 'D'
                y-=1
                x+=1
        elif pos == "D":
            arr[x][y] = num
            x+=1
            if x == N or arr[x][y] != 0:
                pos = 'L'
                x-=1
                y-=1
        elif pos == "L":
            arr[x][y] = num
            y-=1
            if y == -1 or arr[x][y] != 0:
                pos = "U"
                y+=1
                x-=1
        elif pos == "U":
            arr[x][y] = num
            x-=1
            if x == -1 or arr[x][y] != 0:
                pos = "R"
                x+=1
                y+=1
        num+=1
    print(f"#{tc}")
    for i in arr:
        for j in i:
            print(j, end=' ')
        print()