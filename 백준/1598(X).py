import sys
input = sys.stdin.readline
first, second = map(int, input().split())
print((second//4 - first//4) + abs(second%4 - first%4))

# https://www.acmicpc.net/problem/1598