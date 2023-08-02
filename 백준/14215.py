import sys
input = sys.stdin.readline
num = sorted(list(map(int, input().split())))
if num[0] + num[1] > num[2]:
    print(sum(num))
else:
    print((num[0] + num[1]) * 2 - 1)