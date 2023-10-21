import sys
input = sys.stdin.readline
A, B, C = map(int, input().split())
_list = [A, B, C]
if _list.count(1) > _list.count(2): print(1)
else: print(2)