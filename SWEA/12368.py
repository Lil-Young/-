# 24시간 / D3

T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    c = a+b
    if a+b >= 24:
        c %= 24
    print(f"#{tc} {c}")

    