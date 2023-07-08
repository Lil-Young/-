import sys
input = sys.stdin.readline
N = int(input())
F = int(input())
result = F * (N//F)
str_N = str(N); str_N = str_N[:(len(str_N)-2)] + "00"; N = int(str_N)
while True:
    if result < N : break
    result = result - F
result = result + F
result = str(result)
print(result[-2:])

# https://www.acmicpc.net/problem/1075