import sys
input = sys.stdin.readline
print("Gnomes:")
for i in range(int(input())):
    _list = list(map(int, input().split()))
    if _list == sorted(_list) or _list == sorted(_list, reverse=True):
        print("Ordered")
    else:
        print("Unordered")
        
# https://www.acmicpc.net/problem/4589