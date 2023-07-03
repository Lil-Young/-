import sys
input = sys.stdin.readline
list1 = []
for i in range(9) :
    a = int(input())
    list1.append(a)
b = max(list1)
print(b)
c = list1.index(max(list1)) + 1
print(c)