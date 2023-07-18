import sys
input = sys.stdin.readline
while True:
    a = int(input())
    if a == 0: break
    sum = 0
    for i in range(a, 0, -1):
        sum+=i
    print(sum)
    
# https://www.acmicpc.net/problem/5341