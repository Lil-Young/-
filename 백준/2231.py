import sys
input = sys.stdin.readline
N = int(input())
cnt = 0
arr = [[i] for i in range(int(N*0.5), N+1)]
for i in range(0, len(arr)) :
    value = arr[i]
    sum = value[0]
    value_list = list(map(int, str(sum)))
    for j in range(len(value_list)) :
        sum += value_list[j]
    if sum == N :
        print(value[0])
        cnt += 1
        break
if cnt == 0 :
    print(0)