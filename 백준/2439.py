# input = sys.stdin.readline 빠르게 하기
import sys
input = sys.stdin.readline
N = int(input())
for i in range(1, N+1) :
    print(str('*'*i).rjust(N))