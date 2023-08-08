import sys
input = sys.stdin.readline
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
print(min(x1+y2, y1+x2))

# https://www.acmicpc.net/problem/11943