import sys
input = sys.stdin.readline
N = int(input()) # 사람의 수, 창문의 수
num_1 = 1
max_val, val = 3, 3
for i in range(1, N+1):
    if N <= max_val:
        print(num_1)
        break
    else:
        val+=2; max_val+=val
        num_1+=1