# 보충학습과 평균 / D3

T = int(input())
for tc in range(1, T+1):
    n = list(map(int, input().split()))
    arr=[]
    cnt=0
    for i in n:
        if i < 40:
            cnt+=1
            continue
        arr.append(i)
    print(f"#{tc} {int((sum(arr)+(40*cnt))/len(n))}")
         