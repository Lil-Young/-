import sys
input = sys.stdin.readline
N, M = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
list1.extend(list2)
for i in sorted(list1):
    print(i, end = ' ')