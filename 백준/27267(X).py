import sys
input = sys.stdin.readline
a, b, c, d = map(int, input().split())
if a*b > c*d: print("M")
elif a*b > c*d: print("P")
else: print("E")

# https://www.acmicpc.net/problem/27267