import sys
input = sys.stdin.readline
_list = []
for i in range(2):
    T, F, S, P, C = map(int, input().split())
    _list.append(T*6 + F*3 + S*2 + P*1 + C*2)
print(_list[0], _list[1])
# https://www.acmicpc.net/problem/24736