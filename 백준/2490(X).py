# 걸이 배 세개, 등 한 개
# 0이 배
# 도는 A, 개는 B...
_list = list(map(int, input().split()))
num = _list.count(0)
if num == 1: print("A")
elif num == 2: print("B")
elif num == 3: print("C")
elif num == 4: print("D")
else: print("E")

# https://www.acmicpc.net/problem/2490