import sys
from math import floor
input = sys.stdin.readline
N = int(input())
attack = list(map(int, input().split()))
avoid = list(map(int, input().split()))
ratio = list(map(float, input().split()))
new_ratio = [x*10 for x in ratio]

result = 0
for i in range(N):
    if ratio[i] >= 1:
        result += floor(attack[i] * new_ratio[i] / 10)
        result -= avoid[i]
    else:
        result += attack[i]
        result -= floor(avoid[i] * new_ratio[i] / 10)
print(result)