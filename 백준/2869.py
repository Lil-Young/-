import sys
input = sys.stdin.readline
A, B, V = map(int, input().split())
day = 0
day = (V-B)/(A-B)
print(int(day) if day == int(day) else int(day)+1)