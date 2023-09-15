import sys
a, b = map(int, input().split())
_list = []
num = 0
for i in range(a):
    text = input().rstrip()
    _list.append(text)
for j in range(b):
    text = input().rstrip()
    if text in _list:
        num+=1
print(num)