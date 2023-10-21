import sys
input = sys.stdin.readline
_list = []
for i in range(int(input())):
    num = int(input())
    _list.append(num)
if len(_list) == 0: avg = 0
else:
    result = sorted(_list)
    per_15 = round(len(result)*0.15) # 15% 구하기
    if per_15 == 0: 
        total = result
    else:
        total = result[per_15:-per_15]
    avg = round(sum(total)/len(total))
print(avg)

# https://www.acmicpc.net/problem/18110