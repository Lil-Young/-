import sys
input = sys.stdin.readline
# 소수구하기
arr = [False, False] + [True]*9998
primes = []
for i in range(2, 10000) :
    if arr[i] :
        primes.append(i)
    for j in range(2*i, 10000, i) :
        arr[j] = False
#메인
T = int(input())
sosu1, sosu2, n_1, n_2 = 0, 0, 0, 0
for i in range(T) :
    n = int(input())
    n_1, n_2 = n//2, n//2
    while True :
        if n_1 + n_2 == n and n_1 in primes and n_2 in primes :
            print(n_1, n_2)
            break
        else :
            sosu1 = n_1 - 1
            sosu2 = n_2 + 1
            n_1 = sosu1
            n_2 = sosu2
        if n_1 in primes and n_2 in primes :
            print(n_1, n_2)
            break