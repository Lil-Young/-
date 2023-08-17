import sys
input = sys.stdin.readline
N, W, H, L = map(int, input().split())
print(min((W//L) * (H//L), N))

# https://www.acmicpc.net/problem/10698