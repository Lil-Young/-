# 암호 생성기 / D3

for tc in range(1, 11):
    t = int(input())
    arr = list(map(int, input().split()))
    cnt, val = 1, 1
    while val > 0:
        if cnt == 6:
            cnt=1
        val = arr.pop(0)
        val-=cnt
        if val < 0:
            val = 0
        arr.append(val)
        cnt+=1
    print(f"#{tc}", end=' ')
    for i in arr:
        print(i, end=' ')
    print()