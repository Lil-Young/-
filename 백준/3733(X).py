import sys
input = sys.stdin.readline
while True:
    try:
        a, b = map(int, input().split())
    except EOFError:
        break
    else:
        print(b//(a+1))
        
# https://www.acmicpc.net/problem/3733