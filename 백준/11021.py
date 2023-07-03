import sys
input = sys.stdin.readline
T = int(input())
for x in range(1, T+1) :
    A, B = map(int, input().split())
    print("Case #%d:" %x, A+B)