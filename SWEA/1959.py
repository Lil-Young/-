# 두 개의 숫자열 / D2

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # a길이 < b길이
    if n > m:
        temp = b.copy()
        b = a.copy()
        a = temp

    f = (len(b) - len(a)) + 1
    result = 0
    for i in range(f):
        total = 0
        an = 0
        for j in range(i, i+len(a)):
            total += (a[an] * b[j])
            an+=1
        if total > result:
            result = total
    print(f"#{tc} {result}")