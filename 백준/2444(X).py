import sys
input = sys.stdin.readline
num = int(input())
a = 1
for i in range(1, num*2, 2):
    k = num-a
    print(" "*k+"*"*i+" "*k)
    a+=1
a = 4
for i in range(num*2-3, 0 , -2):
    k = num-a
    print(" "*k+"*"*i+" "*k)
    a-=1

# https://www.acmicpc.net/problem/2444
