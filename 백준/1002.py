import sys, math
input = sys.stdin.readline
T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().rstrip().split())
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    r_list = []; r_list.extend([distance, r1, r2])
    max_r = max(r_list); r_list.remove(max_r)
    if distance == 0 and r1 == r2 :
        print(-1)
    elif distance == r1+r2 or max_r == sum(r_list):
        print(1)
    elif max_r > sum(r_list):
        print(0)
    else :
        print(2)