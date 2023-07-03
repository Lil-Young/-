T = int(input())
a_score = 0; b_score = 0
for i in range(T) :
    for j in range(9) :
        a, b = map(int, input().split())
        a_score += a
        b_score += b
    if a_score > b_score :
        print("Yonsei")
    elif a_score < b_score :
        print("Korea")
    else :
        print("Draw")