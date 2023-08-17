import sys
input = sys.stdin.readline
m = int(input())
d = int(input())
if (m <= 2 and d < 18) or m == 1 :
    print("Before")
elif m == 2 and d == 18:
    print("Special")
else :
    print("After")
    
# https://www.acmicpc.net/problem/10768