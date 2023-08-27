import sys
input = sys.stdin.readline
for i in range(int(input())):
    num1, num2 = 0, 0
    word = input().rstrip()
    for j in word:
        if j == '(':
            num1+=1
        elif j == ')':
            num2+=1
        if num1 == num2:
            num1, num2 = 0, 0
    if num1 != 0 or num2 !=0: print("NO")
    else: print("YES")

# https://www.acmicpc.net/problem/9012