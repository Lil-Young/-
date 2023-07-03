import sys
input = sys.stdin.readline
N = int(input())
a = int(input())
a = list(str(a))
sum = 0
for i in range(len(a)) :
    a[i] = int(a[i])
    sum += a[i]
print(sum)