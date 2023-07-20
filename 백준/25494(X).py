import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    arr = list(map(int, input().split()))
    print(min(arr))
    
# https://www.acmicpc.net/problem/25494