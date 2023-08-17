import sys
input = sys.stdin.readline
N = int(input())
_set = set(map(int, input().split()))
for i in _set:
    print(i, end=' ')
    
# https://www.acmicpc.net/problem/10867