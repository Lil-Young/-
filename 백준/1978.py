import sys
input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
solo_sum = 0
for i in num :
    cnt = 0
    for j in range(2, 1001) :
        if i%j == 0 :
            cnt += 1
    if cnt == 1 :
        solo_sum += 1
print(solo_sum)
