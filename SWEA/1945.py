# # 간단한 소인수 분해 / D2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dic = {2:0, 3:0, 5:0, 7:0, 11:0}
    while N != 1:
        if N%2 == 0:
            N //= 2
            dic[2]+=1
        if N%3 == 0:
            N //= 3
            dic[3]+=1
        if N%5 == 0:
            N //= 5
            dic[5]+=1
        if N%7 == 0:
            N //= 7
            dic[7]+=1
        if N%11 == 0:
            N //= 11
            dic[11]+=1
    result = list(dic.values())
    print(f"#{tc} {result[0]} {result[1]} {result[2]} {result[3]} {result[4]}")

