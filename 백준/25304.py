total = int(input())
num = int(input())
sum = 0
for _ in range(num) :
    a, b = map(int, input().split())
    sum += a*b
if total == sum :
    print("Yes")
else :
    print("No")
