import sys
input = sys.stdin.readline
T = int(input())
_list = []
for i in range(T):
    N = int(input())
    if N == 0 : _list.remove(_list[-1])
    else : _list.append(N)
print(sum(_list))

# https://www.acmicpc.net/problem/10773