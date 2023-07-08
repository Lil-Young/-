import sys
input = sys.stdin.readline
word = input().rstrip()
num1 = word[0]; num2 = word[4]; num3 = word[-1]
if num1+num2 == 3:
    print("YES")
else:
    print("NO")
    
# https://www.acmicpc.net/problem/26531