# View / D3

for tc in range(1, 11):
    n = int(input())
    view = list(map(int, input().split()))
    total = 0
    for i in range(2, n-2):
        a = max([view[i-1], view[i-2], view[i+1], view[i+2]])
        if a < view[i]:
            total += (view[i]-a)
    print(f"#{tc} {total}")