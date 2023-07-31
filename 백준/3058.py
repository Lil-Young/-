import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    a = list(map(int, input().split()))
    total, _list = 0, []
    for i in a:
        if i%2 == 0:
            total+=i
            _list.append(i)
    print(total, min(_list))