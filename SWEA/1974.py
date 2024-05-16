# 스도쿠 검증 / D2

T = int(input())
for tc in range(1, T+1):
    result = 1
    arr = []
    for _ in range(9):
        arr.append(list(map(int, input().split())))
    for i in range(9):
        x_dic = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
        y_dic = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
        for j in range(9):
            x_dic[arr[i][j]]+=1
            y_dic[arr[j][i]]+=1
        if list(x_dic.values()).count(1) != 9 or list(y_dic.values()).count(1) != 9:
            result = 0
            break
    index = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
    for start in index:
        dic = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
        x, y = start[0], start[1]
        for i in range(3):
            for j in range(3):
                dic[arr[x][y]]+=1
                y+=1
            y=start[1]
            x+=1
        if list(dic.values()).count(1) != 9:
            result = 0
            break
    print(f"#{tc} {result}")