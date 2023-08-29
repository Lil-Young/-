import sys
input = sys.stdin.readline
T = int(input())
val = list(map(int, input().split()))
for i in range(3, 1000000):
    total = 0
    for j in val:
        if i%j == 0:
            total+=1
    if total == len(val):
        result = i
        break
print(result)

# https://www.acmicpc.net/problem/1037