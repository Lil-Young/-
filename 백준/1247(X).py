import sys
input = sys.stdin.readline
for i in range(3):
    _list = []
    T = int(input())
    for j in range(T):
        num = int(input())
        _list.append(num)
    if sum(_list) > 0 : print("+")
    elif sum(_list) == 0 : print(0)
    elif sum(_list) < 0 : print("-")

# https://www.acmicpc.net/problem/1247