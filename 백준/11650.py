import sys
input = sys.stdin.readline
_list = []
for i in range(int(input())):
    a = list(map(int, input().split()))
    _list.append(a)
for i in sorted(_list):
    for j in i:
        print(j, end=' ')
    print()