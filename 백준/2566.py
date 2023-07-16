import sys
input = sys.stdin.readline
_list = [list(map(int, input().split())) for _ in range(9)]
total = []
for i in range(9) :
    for j in _list[i] :
        total.append(j)

for i in range(9) :
    for j in range(9) :
        if _list[i][j] == max(total) :
            print(max(total))
            print(i+1, j+1)
            break