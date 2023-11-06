import sys
input = sys.stdin.readline
N, M = map(int, input().split())
_list = [N, M]
print(min(_list)//2)