K, N, M = map(int, input().split())
result = K*N - M
if K*N < M :
    print(0)
else : 
    print(result)