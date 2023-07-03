T = int(input())
A = 300; B = 60; C = 10
A_cnt = 0; B_cnt = 0; C_cnt = 0
while True :
    if T % C != 0 :
        print(-1)
        break
    else :
        if T >= A :
            A_cnt += 1
            T -= A
        elif T >= B :
            B_cnt += 1
            T -= B
        elif T >= C :
            C_cnt += 1
            T -= C
    if T == 0 :
        print(A_cnt, B_cnt, C_cnt)
        break