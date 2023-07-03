import sys
input = sys.stdin.readline
T = int(input())
result = 0
for i in range(T) :
    A, B = map(int, input().split())
    result = A + B
    print(result)