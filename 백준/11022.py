# input = sys.stdin.readline 빠르게 하기
import sys
input = sys.stdin.readline
T = int(input())
for x in range(1, T+1) :
    A, B = map(int, input().split())
    C = A+B
    print("Case #%d: %d + %d = %d" %(x, A, B, C))
