# 백만 장자 프로젝트 / D2

T = int(input())
for i in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    total = 0
    num = a[N-1]
    for j in range(N-2, -1, -1):
        if a[j] > num:
            num = a[j]
        total += (num - a[j])
    print(f"#{i} {total}")
