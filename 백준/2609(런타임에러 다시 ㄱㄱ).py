import sys
input = sys.stdin.readline
a, b = map(int, input().split())
# 최대공약수 구하기
for i in range(10001, 1, -1):
    if a%i == 0 and b%i == 0:
        result1 = i
        break
# 최소공배수 구하기, 최소공배수 = 두 자연수의 곱/최대공약수
result2 = a*b//result1
print(result1)
print(result2)

# https://www.acmicpc.net/problem/2609