import sys
input = sys.stdin.readline
N = int(input())
x_list = []
y_list = []
for i in range(N):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
min_x, max_x = min(x_list), max(x_list)
min_y, max_y = min(y_list), max(y_list)
print((max_x-min_x) * (max_y-min_y))