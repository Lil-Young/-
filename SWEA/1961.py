# 숫자 배열 회전 / D2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    # 90도
    a = []
    for i in range(N):
        s = ""
        for j in range(N-1, -1, -1):
            s+=str(arr[j][i])
        a.append(s)
    # 180도
    b = []
    for i in range(N-1, -1, -1):
        s = ""
        for j in range(N-1, -1, -1):
            s+=str(arr[i][j])
        b.append(s)
    # 270도
    c = []
    for i in range(N-1, -1, -1):
        s = ""
        for j in range(N):
            s+=str(arr[j][i])
        c.append(s)
    print(f"#{tc}")
    for r in zip(a, b, c):
        print(r[0], r[1], r[2])