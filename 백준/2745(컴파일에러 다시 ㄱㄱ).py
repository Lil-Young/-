import sys
input = sys.stdin.readline
N, B = input().split()
print(int(B)**len(N)-1)

# https://www.acmicpc.net/problem/2745