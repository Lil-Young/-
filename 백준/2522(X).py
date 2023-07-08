import sys
input = sys.stdin.readline
T = int(input())
for i in range(1, T+1):
    print(" "*(T-i)+"*"*i)
for j in range(T-1, 0, -1):
    print(" "*(T-j)+"*"*j)
    
# https://www.acmicpc.net/problem/2522