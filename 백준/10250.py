import sys
input = sys.stdin.readline
n = int(input().rstrip())
for m in range(n) :
    H, W, N = map(int, input().split())
    # 호텔의 층수, 각층의 방 수, 몇번째 손님
    i = 0 # 몇번째 손님
    j = 1 # 호실
    k = 0 # 층수
    while N>i :
        i+=1
        k+=1
        if H<k :
            k-=H
            j+=1
    if j < 10 :
        j = "0" + str(j)
    print(str(k)+str(j))