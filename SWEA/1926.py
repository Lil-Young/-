# 간단한 369게임 / D2

N = int(input())
for i in range(1, N+1):
    list_n = list(str(i))
    total = 0
    if '3' in list_n or '6' in list_n or '9' in list_n:
        total += (list_n.count('3') + list_n.count('6') + list_n.count('9'))
    if total == 0:
        print(i, end=' ')
        continue
    print('-'*total, end=' ')