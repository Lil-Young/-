import sys
input = sys.stdin.readline
_list = []
for i in range(int(input())):
    a, d, g = map(int, input().split())
    grade = a*(d+g)
    if a == d+g:
        _list.append(grade*2)
    else :
        _list.append(grade)
print(max(_list))

# https://www.acmicpc.net/problem/25600