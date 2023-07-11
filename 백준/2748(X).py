import sys
input = sys.stdin.readline
n = int(input())
count = 0
num1, num2 = 0, 1
for i in range(n-1):
    if i == n: break
    num = num1+num2
    num1 = num2
    num2 = num    
print(num)
        
    


# https://www.acmicpc.net/problem/2748