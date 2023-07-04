import sys
input = sys.stdin.readline
num = []
for i in range(7):
    a = int(input())
    if a%2 == 1 :
        num.append(a)
    else: pass
if len(num) == 0 :
    print(-1)
else : 
    print(sum(num))
    print(min(num))
    
# https://www.acmicpc.net/problem/2576