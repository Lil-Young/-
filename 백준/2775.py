T= int(input())
for _ in range(T) :
    k = int(input()) # 층 수
    n = int(input()) # 호실
    # k = 0 이면 n은 사람 수
    num = 2
    a = [[0 for _ in range(n+1)] for _ in range(k+1)]
    for i in range(0, k+1, 1) :
        for j in range(0, n+1, 1) :
            if j == 0 :
                a[i][j] = 1
            elif i == 0 :
                a[i][j] += num
                num += 1
            else :    
                a[i][j] = a[i-1][j] + a[i][j-1]
            #a[k][n] = a[k-1] + a[n-1]
    print(a[k][n-1])