import sys
input = sys.stdin.readline
N = int(input())
for i in range(N) :
    a = list(input())
    sum, count = 0, 0
    for j in range(len(a)) :
        if a[j] == 'O' :
            count = count + 1
            sum += count
        elif a[j] == 'X' :
            count = 0
    print(sum)
