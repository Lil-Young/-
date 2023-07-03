import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
M = max(arr)
Total = 0
for j in range(N) :
    arr[j] = arr[j]/M*100
    Total += arr[j]
avg = Total / N
print(avg)