N = int(input())
hansu = 0
a = []
for i in range(1, N+1) :
    if i < 100 :
        hansu += 1
    else :
        i = list(map(int, str(i)))
        if i[0]-i[1] == i[1]-i[2] :
            hansu += 1
print(hansu)