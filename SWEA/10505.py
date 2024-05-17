# 소득 불균형 / D3
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    avg = int(sum(a)/len(a))
    total = 0
    for i in a:
        if i <= avg:
            total+=1
    print(f"#{tc} {total}")