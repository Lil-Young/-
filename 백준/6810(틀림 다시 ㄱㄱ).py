import sys
input = sys.stdin.readline
a = input().rstrip()
b = input().rstrip()
c = input().rstrip()
result = list("9780921418"+a+b+c)
total = 0
count = 0
for i in result:
    if count%2 == 0:
        total += int(i)
    else: 
        total += int(i)*3
    count+=1
print(f"1-3-합은 {total}")

# https://www.acmicpc.net/problem/6810