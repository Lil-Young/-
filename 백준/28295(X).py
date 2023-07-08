import sys
input = sys.stdin.readline
_list = ["N", "E", "S", "W"]
dir = "N"
for i in range(10):
    num = int(input())
    if num == 1: dir = _list[(_list.index(dir) + 1) % 4]
    elif num == 2: dir = _list[(_list.index(dir) + 2) % 4]
    elif num == 3: dir = _list[(_list.index(dir) + 3) % 4]
print(dir)

# https://www.acmicpc.net/problem/28295