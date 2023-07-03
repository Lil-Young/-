import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    c_sum = 0
    temp = input()
    N = int(input())
    for j in range(N) :
        c_num = int(input())
        if c_num >= 0 :
            c_sum += c_num
    if (c_sum % N) == 0:
        print("YES")
    else :
        print("NO")