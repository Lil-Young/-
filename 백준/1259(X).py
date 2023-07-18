import sys
input = sys.stdin.readline
while True:
    a = input().rstrip()
    if a == '0': break
    a = list(a)
    if a == list(reversed(a)): print("yes")
    else: print("no")

# https://www.acmicpc.net/problem/1259