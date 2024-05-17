# 준환이의 운동관리 / D3

T = int(input())
for tc in range(1, T+1):
    L, U, X = map(int, input().split())
    result = 0
    if X < L:
        result = L-X
    elif X >= L and X <= U:
        result = 0
    else:
        result = -1
    print(f"#{tc} {result}")