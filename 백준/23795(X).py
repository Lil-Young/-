import sys
input = sys.stdin.readline
total = 0
while True:
    m = int(input())
    if m == -1: break
    total+=m
print(total)

# https://www.acmicpc.net/problem/23795