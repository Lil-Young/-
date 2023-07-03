from itertools import count
import sys
input = sys.stdin.readline
A = int(input())
B = int(input())
C = int(input())
result = A*B*C
list1 = list(map(int, str(result)))
print(list1.count(0))
print(list1.count(1))
print(list1.count(2))
print(list1.count(3))
print(list1.count(4))
print(list1.count(5))
print(list1.count(6))
print(list1.count(7))
print(list1.count(8))
print(list1.count(9))