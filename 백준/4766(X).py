import sys
input = sys.stdin.readline
a = float(input())
while True:
    b = float(input())
    if b == 999: break
    print("{:.2f}".format(b-a))
    a = b
# https://www.acmicpc.net/problem/4766