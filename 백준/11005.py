import sys
input = sys.stdin.readline
N, B = map(int, input().split())
_list = []
word = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while True:
    _list.append(word[N%B])
    N //= B
    if N == 0 : break
for i in _list[::-1]:
    print(i, end='')