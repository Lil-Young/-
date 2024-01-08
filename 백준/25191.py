import sys
input = sys.stdin.readline
c = int(input())
a, b = map(int, input().split())
result = a//2 + b
if result > c : print(c)
else: print(result)