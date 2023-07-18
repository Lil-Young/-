import sys
input = sys.stdin.readline
_list = []
for i in range(5):
    num = int(input())
    _list.append(num)
a = sorted(_list)
print(sum(a)//len(a), a[len(a)//2])

# https://www.acmicpc.net/problem/2587