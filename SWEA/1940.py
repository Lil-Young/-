# 가랏! RC카! / D2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = 0
    now = 0
    for _ in range(N):
        c = list(map(int, input().split()))
        if c[0] == 1:
            now+=c[1]
        elif c[0] == 2:
            if (now-c[1]) >= 0:
                now-=c[1]
        if now > 0:
            result += now
    print(f"#{tc} {result}")

