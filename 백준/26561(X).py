import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    p, t = map(int, input().split())
    print(p + t//4 - t//7)
    
# https://www.acmicpc.net/problem/26561