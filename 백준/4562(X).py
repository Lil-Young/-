import sys
input = sys.stdin.readline
for i in range(int(input())):
    a, b = map(int, input().split())
    if a >= b: print("MMM BRAINS")
    else : print("NO BRAINS")
    
# https://www.acmicpc.net/problem/4562