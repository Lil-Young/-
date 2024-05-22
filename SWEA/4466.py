# 최대 성적표 만들기 / D3

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(f"#{tc} {sum(a[:k])}")