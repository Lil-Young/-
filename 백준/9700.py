# USB 꽂기의 미스터리 / D3

T = int(input())
for tc in range(1, T+1):
    p, q = map(float, input().split())
    a = (1-p) * q
    b = p * (1-q) * q
    print(f"#{tc}", "YES" if b > a else "NO")