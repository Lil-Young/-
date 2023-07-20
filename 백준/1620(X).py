import sys
input = sys.stdin.readline
n, m = map(int, input().split())
n_list = []
for i in range(n+m):
    a = input().rstrip()
    if i < n: n_list.append(a)
    else: 
        if a[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print(n_list[int(a)-1])
        else: print(n_list.index(a)+1)

# https://www.acmicpc.net/problem/1620