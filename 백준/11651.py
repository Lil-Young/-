import sys
input = sys.stdin.readline
_list = []
for i in range(int(input())):
    a = list(map(int, input().split()))
    _list.append(a)
re_list = []
for i in _list:
    i = list(reversed(i))  
    re_list.append(i)
result = sorted(re_list)

result_list = []
for i in result:
    i = list(reversed(i))  
    result_list.append(i)
for i in result_list:
    print(i[0], i[1])