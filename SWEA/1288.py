# 새로운 불면증 치료법 / D2

T = int(input())
for tc in range(1, T+1):
    arr = [0] * 10
    n = int(input())
    temp = n
    cnt = 0
    while sum(arr) != 10:
        cnt+=1
        n = temp*cnt
        for i in str(n):
            if arr[int(i)] == 0:
                arr[int(i)]+=1
    print(f"#{tc} {temp*cnt}")