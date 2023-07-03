import sys
input = sys.stdin.readline
x, y, w, h = map(int, input().split())
val_list = []
val_list.extend([h-y, y, w-x, x])
print(min(val_list))