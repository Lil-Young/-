import sys
input = sys.stdin.readline
T = int(input())
_list = [None, True, None, None]
for i in range(T):
    a, b = map(int, input().split())
    temp = _list[a]
    _list[a] = _list[b]
    _list[b] = temp
if True in _list :
    print(_list.index(True))
else: print(-1)

# https://www.acmicpc.net/problem/1547