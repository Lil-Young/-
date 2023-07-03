import sys
input = sys.stdin.readline
arr1 = []
for j in range(42) :
    arr1.append(0)
for i in range(10) :
    num = int(input())
    arr1[num%42] += 1
cnt = 0
for k in range(42) :
    if arr1[k] != 0 :
        cnt +=1
print(cnt)
