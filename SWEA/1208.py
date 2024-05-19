# Flatten / D3

for tc in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    for _ in range(n):
        imax = arr.index(max(arr))
        imin = arr.index(min(arr))
        arr[imax]-=1
        arr[imin]+=1
    print(f"#{tc} {max(arr)-min(arr)}")