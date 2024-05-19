# 직사각형 길이 찾기 / D3

T = int(input())
for tc in range(1, T+1):
    a = list(map(int, input().split()))
    target = list(set(a))
    if a.count(target[0]) == 1 or a.count(target[0]) == 3:
        print(f"#{tc} {target[0]}")
    else:
        print(f"#{tc} {target[1]}")