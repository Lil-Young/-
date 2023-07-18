import sys
input = sys.stdin.readline
a = input().rstrip()
a = list(a)
a.sort(reverse=True)
for i in a:
    print(i, end='')

# https://www.acmicpc.net/problem/1427