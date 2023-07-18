import sys
input = sys.stdin.readline
_list = []
for i in range(int(input())):
    a = int(input())
    _list.append(a)
for i in sorted(_list):
    print(i)

# https://www.acmicpc.net/problem/2751