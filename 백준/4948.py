arr = [False, False] + [True]*256892
primes = []
for i in range(2, 256892) :
    if arr[i] :
        primes.append(i)
    for j in range(2*i, 256892, i) :
        arr[j] = False
while True :
    N = int(input())
    if N == 0 :
        break
    count = 0
    for i in primes :
        if N < i < N*2+1 :
            count+=1
    print(count)