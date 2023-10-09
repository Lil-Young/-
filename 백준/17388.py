import sys
input = sys.stdin.readline
S, K, H = map(int, input().split())
_list = [S, K, H]
if S+K+H >= 100: print("OK")
else: 
    min_num = min(_list)
    index = _list.index(min_num)
    if index == 0: print("Soongsil")
    elif index == 1: print("Korea")
    else: print("Hanyang")