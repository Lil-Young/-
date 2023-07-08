import sys
input = sys.stdin.readline
N = int(input())
total = 0
for i in range(N):
    p = int(input())
    total += p
print(total - (N-1))

# https://www.acmicpc.net/problem/2010