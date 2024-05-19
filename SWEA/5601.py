# 쥬스 나누기 / D3

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    p, q = 1, N
    print(f"#{tc}", end=' ')
    for _ in range(N):
        print(f"{p}/{q}", end=' ')
    print()